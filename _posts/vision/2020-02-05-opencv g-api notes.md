---
categories: vision
---
[TOC]

# Intro

lots of template programming are used



# g-api notes

```cpp

class GAPI_EXPORTS GMat
{
public:
    GMat();                                 // Empty constructor
    GMat(const GNode &n, std::size_t out);  // Operation result constructor

    GOrigin& priv();                        // Internal use only
    const GOrigin& priv()  const;           // Internal use only

private:
    std::shared_ptr<GOrigin> m_priv;
};
```

# Q: What is GOrigin? What the meaning of parameters GMat(const GNode &n, std::size_t out)


A: It seems GOrigin means the source of a edge, it consists of 2 parts: from which node's which index (a node may have multiple outputs?)


```cpp

#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/gapi.hpp>
#include <opencv2/gapi/core.hpp>
#include <opencv2/gapi/imgproc.hpp>

int main(int argc, char *argv[])
{
    cv::VideoCapture cap;
    if (argc > 1) cap.open(argv[1]);
    else cap.open(0);
    CV_Assert(cap.isOpened());

    cv::GMat in;
    cv::GMat vga      = cv::gapi::resize(in, cv::Size(), 0.5, 0.5);
    cv::GMat gray     = cv::gapi::BGR2Gray(vga);
    cv::GMat blurred  = cv::gapi::blur(gray, cv::Size(5,5));
    cv::GMat edges    = cv::gapi::Canny(blurred, 32, 128, 3);
    cv::GMat b,g,r;
    std::tie(b,g,r)   = cv::gapi::split3(vga);
    cv::GMat out      = cv::gapi::merge3(b, g | edges, r);
    cv::GComputation ac(in, out);
    
    cv::Mat input_frame;
    cv::Mat output_frame;
    CV_Assert(cap.read(input_frame));
    do
    {
        ac.apply(input_frame, output_frame);
        cv::imshow("output", output_frame);
    } while (cap.read(input_frame) && cv::waitKey(30) < 0);
    
    return 0;
}

```

# Q: how does cv::Mat convert to cv::gapi::own::Mat? how memory is handled?

A: when break down to the apply() function. the paramaters are converted to:


```cpp

>	opencv_world400d.dll!cv::GComputation::apply(
	std::vector[cv::util::variant[cv::Mat,cv::Scalar_[double],cv::UMat,cv::gapi::own::Mat,cv::gapi::own::Scalar,cv::detail::VectorRef],std::allocator[cv::util::variant[cv::Mat,cv::Scalar_[double],cv::UMat,cv::gapi::own::Mat,cv::gapi::own::Scalar,cv::detail::VectorRef] ] ] && ins, 
	std::vector[cv::util::variant[cv::Mat *,cv::Scalar_[double] *,cv::UMat *,cv::gapi::own::Mat *,cv::gapi::own::Scalar *,cv::detail::VectorRef],std::allocator[cv::util::variant[cv::Mat *,cv::Scalar_[double] *,cv::UMat *,cv::gapi::own::Mat *,cv::gapi::own::Scalar *,cv::detail::VectorRef] ] ] && outs, 
	std::vector[cv::GCompileArg,std::allocator[cv::GCompileArg] ] && args) Line 102	C++

void cv::GComputation::apply(GRunArgs &&ins, GRunArgsP &&outs, GCompileArgs &&args)
{
    const auto in_metas = descr_of(ins);
    // FIXME Graph should be recompiled when GCompileArgs have changed
    if (m_priv->m_lastMetas != in_metas)
    {
        if (m_priv->m_lastCompiled &&
            m_priv->m_lastCompiled.canReshape() &&
            formats_are_same(m_priv->m_lastMetas, in_metas))
        {
            m_priv->m_lastCompiled.reshape(in_metas, args);
        }
        else
        {
            // FIXME: Had to construct temporary object as compile() takes && (r-value)
            m_priv->m_lastCompiled = compile(GMetaArgs(in_metas), std::move(args));
        }
        m_priv->m_lastMetas = in_metas;
    }
    m_priv->m_lastCompiled(std::move(ins), std::move(outs));
}

```

cv::GComputation ac(in, out);
ac.apply(input_frame, output_frame);

# Q: Why not compile in GComputation ctor, but in apply()?

A: (may) because only when apply the input shape can be determined

m_priv->m_lastCompiled = compile(GMetaArgs(in_metas), std::move(args));

# Q:  Why compile inputs is in_metas but not out_metas?

A: because use in_metas to determine graph's every node's shapes


```cpp

cv::gimpl::GCompiler::GCompiler(const cv::GComputation &c,
                                GMetaArgs              &&metas,
                                GCompileArgs           &&args)
    : m_c(c), m_metas(std::move(metas)), m_args(std::move(args))
{
    using namespace std::placeholders;
    m_all_kernels       = getKernelPackage(m_args);
    auto lookup_order   = getCompileArg<gapi::GLookupOrder>(m_args).value_or(gapi::GLookupOrder());
    auto dump_path      = getGraphDumpDirectory(m_args);

    m_e.addPassStage("init");
    m_e.addPass("init", "check_cycles",  ade::passes::CheckCycles());
    m_e.addPass("init", "expand_kernels",  std::bind(passes::expandKernels, _1,
                                                     m_all_kernels)); // NB: package is copied
    m_e.addPass("init", "topo_sort",     ade::passes::TopologicalSort());
    m_e.addPass("init", "init_islands",  passes::initIslands);
    m_e.addPass("init", "check_islands", passes::checkIslands);
    // TODO:
    // - Check basic graph validity (i.e., all inputs are connected)
    // - Complex dependencies (i.e. parent-child) unrolling
    // - etc, etc, etc
    
    // Remove GCompoundBackend to avoid calling setupBackend() with it in the list
    m_all_kernels.remove(cv::gapi::compound::backend());
    m_e.addPass("init", "resolve_kernels", std::bind(passes::resolveKernels, _1,
                                                     std::ref(m_all_kernels), // NB: and not copied here
                                                     lookup_order));
    
    m_e.addPass("init", "check_islands_content", passes::checkIslandsContent);
    m_e.addPassStage("meta");
    m_e.addPass("meta", "initialize",   std::bind(passes::initMeta, _1, std::ref(m_metas)));
    m_e.addPass("meta", "propagate",    std::bind(passes::inferMeta, _1, false));
    m_e.addPass("meta", "finalize",     passes::storeResultingMeta);
    // moved to another stage, FIXME: two dumps?
    //    m_e.addPass("meta", "dump_dot",     passes::dumpDotStdout);
    
    // Special stage for backend-specific transformations
    // FIXME: document passes hierarchy and order for backend developers
    m_e.addPassStage("transform");
    
    m_e.addPassStage("exec");
    m_e.addPass("exec", "fuse_islands",     passes::fuseIslands);
    m_e.addPass("exec", "sync_islands",     passes::syncIslandTags);
    
    if (dump_path.has_value())
    {
        m_e.addPass("exec", "dump_dot", std::bind(passes::dumpGraph, _1,
                                                  dump_path.value()));
    }
    
    // Process backends at the last moment (after all G-API passes are added).
    ade::ExecutionEngineSetupContext ectx(m_e);
    auto backends = m_all_kernels.backends();
    for (auto &b : backends)
    {
        b.priv().addBackendPasses(ectx);
    }
}

```

# Q: How does ade work? What is the meaning of these passes, eg

A: TODO???	


```cpp

   m_e.addPass("init", "check_cycles",  ade::passes::CheckCycles());
    m_e.addPass("init", "expand_kernels",  std::bind(passes::expandKernels, _1,
                                                     m_all_kernels)); // NB: package is copied
    m_e.addPass("init", "topo_sort",     ade::passes::TopologicalSort());
    m_e.addPass("init", "init_islands",  passes::initIslands);
    m_e.addPass("init", "check_islands", passes::checkIslands);


```

# Q: How to impl a resize() operator?

A: ???

```cpp
// core.hpp
G_TYPED_KERNEL(GResize, <GMat(GMat,Size,double,double,int)>, "org.opencv.core.transform.resize") {
        static GMatDesc outMeta(GMatDesc in, Size sz, double fx, double fy, int) {
            if (sz.width != 0 && sz.height != 0)
            {
                return in.withSize(sz);
            }
            else
            {
                GAPI_Assert(fx != 0. && fy != 0.);
                return in.withSize
                    (Size(static_cast<int>(std::round(in.size.width  * fx)),
                          static_cast<int>(std::round(in.size.height * fy))));
            }
        }
    };

GAPI_EXPORTS GMat resize(const GMat& src, const Size& dsize, double fx = 0, double fy = 0, int interpolation = INTER_LINEAR);

// kernels_core.cpp
GMat resize(const GMat& src, const Size& dsize, double fx, double fy, int interpolation)
{
    return core::GResize::on(src, dsize, fx, fy, interpolation);
}

// gcpucore.cpp
GAPI_OCV_KERNEL(GCPUResize, cv::gapi::core::GResize)
{
    static void run(const cv::Mat& in, cv::Size sz, double fx, double fy, int interp, cv::Mat &out)
    {
        cv::resize(in, out, sz, fx, fy, interp);
    }
};
```

- [ ] G_TYPED_KERNEL
- [ ] GResize
  - [ ] core::GResize::on
- [x] GAPI_OCV_KERNEL
  - [ ] GCPUKernelImpl

```cpp
#define GAPI_OCV_KERNEL(Name, API) struct Name: public cv::GCPUKernelImpl<Name, API>

// gkernel.hpp

```



# What is `core::GResize::on`

It actually calls

```cpp
template<typename K, typename R, typename... Args>
class GKernelType<K, std::function<R(Args...)> >:
        public detail::MetaHelper<K, std::tuple<Args...>, R >
{
public:
    using InArgs  = std::tuple<Args...>;
    using OutArgs = std::tuple<R>;

    static R on(Args... args)
    {
        cv::GCall call(GKernel{K::id(), &K::getOutMeta, {detail::GTypeTraits<R>::shape}});
        call.pass(args...);
        return detail::Yield<R>::yield(call, 0);
    }
};
```



# Q: How is registered kernels dispatched?

A:refer following callstack

```cpp
 	opencv_world400d.dll!GCPUCanny::run(const cv::Mat & in, double thr1, double thr2, int apSize, bool l2gradient, cv::Mat & out) Line 161	C++
 	opencv_world400d.dll!cv::detail::OCVCallHelper<GCPUCanny,std::tuple<cv::GMat,double,double,int,bool>,std::tuple<cv::GMat> >::call_and_postprocess<cv::Mat,double,double,int,bool>::call<cv::detail::tracked_cv_mat>(cv::Mat && <ins_0>, double && <ins_1>, double && <ins_2>, int && <ins_3>, bool && <ins_4>, cv::detail::tracked_cv_mat && <outs_0>) Line 224	C++
 	opencv_world400d.dll!cv::detail::OCVCallHelper<GCPUCanny,std::tuple<cv::GMat,double,double,int,bool>,std::tuple<cv::GMat> >::call_impl<0,1,2,3,4,0>(cv::GCPUContext & ctx, cv::detail::Seq<0,1,2,3,4> __formal, cv::detail::Seq<0> __formal) Line 237	C++
 	opencv_world400d.dll!cv::detail::OCVCallHelper<GCPUCanny,std::tuple<cv::GMat,double,double,int,bool>,std::tuple<cv::GMat> >::call(cv::GCPUContext & ctx) Line 245	C++
 	opencv_world400d.dll!std::_Invoker_functor::_Call<void (__cdecl*& __ptr64)(cv::GCPUContext & __ptr64),cv::GCPUContext & __ptr64>(void(*)(cv::GCPUContext &) & _Obj, cv::GCPUContext & <_Args_0>) Line 1377	C++
 	opencv_world400d.dll!std::invoke<void (__cdecl*& __ptr64)(cv::GCPUContext & __ptr64),cv::GCPUContext & __ptr64>(void(*)(cv::GCPUContext &) & _Obj, cv::GCPUContext & <_Args_0>) Line 1445	C++
 	opencv_world400d.dll!std::_Invoke_ret<void,void (__cdecl*& __ptr64)(cv::GCPUContext & __ptr64),cv::GCPUContext & __ptr64>(std::_Forced<void,1> __formal, void(*)(cv::GCPUContext &) & <_Vals_0>, cv::GCPUContext & <_Vals_1>) Line 1462	C++
 	opencv_world400d.dll!std::_Func_impl<void (__cdecl*)(cv::GCPUContext & __ptr64),std::allocator<int>,void,cv::GCPUContext & __ptr64>::_Do_call(cv::GCPUContext & <_Args_0>) Line 214	C++
 	opencv_world400d.dll!std::_Func_class<void,cv::GCPUContext & __ptr64>::operator()(cv::GCPUContext & <_Args_0>) Line 280	C++
 	opencv_world400d.dll!cv::GCPUKernel::apply(cv::GCPUContext & ctx) Line 52	C++
 	opencv_world400d.dll!cv::gimpl::GCPUExecutable::run(std::vector<std::pair<cv::gimpl::RcDesc,cv::util::variant<cv::Mat,cv::Scalar_<double>,cv::UMat,cv::gapi::own::Mat,cv::gapi::own::Scalar,cv::detail::VectorRef> >,std::allocator<std::pair<cv::gimpl::RcDesc,cv::util::variant<cv::Mat,cv::Scalar_<double>,cv::UMat,cv::gapi::own::Mat,cv::gapi::own::Scalar,cv::detail::VectorRef> > > > && input_objs, std::vector<std::pair<cv::gimpl::RcDesc,cv::util::variant<cv::Mat *,cv::Scalar_<double> *,cv::UMat *,cv::gapi::own::Mat *,cv::gapi::own::Scalar *,cv::detail::VectorRef> >,std::allocator<std::pair<cv::gimpl::RcDesc,cv::util::variant<cv::Mat *,cv::Scalar_<double> *,cv::UMat *,cv::gapi::own::Mat *,cv::gapi::own::Scalar *,cv::detail::VectorRef> > > > && output_objs) Line 210	C++
>	opencv_world400d.dll!cv::gimpl::GExecutor::run(cv::gimpl::GRuntimeArgs && args) Line 213	C++
 	opencv_world400d.dll!cv::GCompiled::Priv::run(cv::gimpl::GRuntimeArgs && args) Line 39	C++
 	opencv_world400d.dll!cv::GCompiled::operator()(std::vector<cv::util::variant<cv::Mat,cv::Scalar_<double>,cv::UMat,cv::gapi::own::Mat,cv::gapi::own::Scalar,cv::detail::VectorRef>,std::allocator<cv::util::variant<cv::Mat,cv::Scalar_<double>,cv::UMat,cv::gapi::own::Mat,cv::gapi::own::Scalar,cv::detail::VectorRef> > > && ins, std::vector<cv::util::variant<cv::Mat *,cv::Scalar_<double> *,cv::UMat *,cv::gapi::own::Mat *,cv::gapi::own::Scalar *,cv::detail::VectorRef>,std::allocator<cv::util::variant<cv::Mat *,cv::Scalar_<double> *,cv::UMat *,cv::gapi::own::Mat *,cv::gapi::own::Scalar *,cv::detail::VectorRef> > > && outs) Line 95	C++
 	opencv_world400d.dll!cv::GComputation::apply(std::vector<cv::util::variant<cv::Mat,cv::Scalar_<double>,cv::UMat,cv::gapi::own::Mat,cv::gapi::own::Scalar,cv::detail::VectorRef>,std::allocator<cv::util::variant<cv::Mat,cv::Scalar_<double>,cv::UMat,cv::gapi::own::Mat,cv::gapi::own::Scalar,cv::detail::VectorRef> > > && ins, std::vector<cv::util::variant<cv::Mat *,cv::Scalar_<double> *,cv::UMat *,cv::gapi::own::Mat *,cv::gapi::own::Scalar *,cv::detail::VectorRef>,std::allocator<cv::util::variant<cv::Mat *,cv::Scalar_<double> *,cv::UMat *,cv::gapi::own::Mat *,cv::gapi::own::Scalar *,cv::detail::VectorRef> > > && outs, std::vector<cv::GCompileArg,std::allocator<cv::GCompileArg> > && args) Line 120	C++
 	opencv_world400d.dll!cv::GComputation::apply(cv::Mat in, cv::Mat & out, std::vector<cv::GCompileArg,std::allocator<cv::GCompileArg> > && args) Line 140	C++
 	testGapi.exe!main(int argc, char * * argv) Line 33	C++

```



# GMatDesc

## Q: What's purpose of outMeta()

It is called by `void cv::gimpl::passes::inferMeta(ade::passes::PassContext &ctx, bool meta_is_initialized)`.  It is described as:

// Iterate over all operations in the topological order, trigger kernels
// validate() function, update output objects metadata.

## Q: How is outMeta() called

```cpp
    G_TYPED_KERNEL_M(GSplit3, <GMat3(GMat)>, "org.opencv.core.transform.split3") {
        static std::tuple<GMatDesc, GMatDesc, GMatDesc> outMeta(GMatDesc in) {
            const auto out_depth = in.depth;
            const auto out_desc  = in.withType(out_depth, 1);
            return std::make_tuple(out_desc, out_desc, out_desc);
        }
    };
```



```cpp
0:000> kpn
 # Child-SP          RetAddr           Call Site
00 00000000`002ed660 000007fe`ac6fed0a opencv_world400d!cv::gapi::core::GResize::outMeta(struct cv::GMatDesc * in = 0x00000000`002ed7e0, class cv::Size_<int> * sz = 0x00000000`002ed780, double fx = 0.5, double fy = 0.5, int __formal = 0n1)+0x32 [c:\build\master_winpack-build-win64-vc14\opencv\modules\gapi\include\opencv2\gapi\core.hpp @ 387] 
01 00000000`002ed6f0 000007fe`ac711eb3 opencv_world400d!cv::detail::MetaHelper<cv::gapi::core::GResize,std::tuple<cv::GMat,cv::Size_<int>,double,double,int>,cv::GMat>::getOutMeta_impl<0,1,2,3,4>(class std::vector<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc>,std::allocator<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc> > > * in_meta = 0x00000000`002edca8 { size=5 }, class std::vector<cv::GArg,std::allocator<cv::GArg> > * in_args = 0x00000000`020f8620 { size=5 }, struct cv::detail::Seq<0,1,2,3,4> __formal = struct cv::detail::Seq<0,1,2,3,4>)+0x18a [c:\build\master_winpack-build-win64-vc14\opencv\modules\gapi\include\opencv2\gapi\gkernel.hpp @ 152] 
02 00000000`002ed860 000007fe`ac6fa559 opencv_world400d!cv::detail::MetaHelper<cv::gapi::core::GResize,std::tuple<cv::GMat,cv::Size_<int>,double,double,int>,cv::GMat>::getOutMeta(class std::vector<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc>,std::allocator<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc> > > * in_meta = 0x00000000`002edca8 { size=5 }, class std::vector<cv::GArg,std::allocator<cv::GArg> > * in_args = 0x00000000`020f8620 { size=5 })+0x53 [c:\build\master_winpack-build-win64-vc14\opencv\modules\gapi\include\opencv2\gapi\gkernel.hpp @ 160] 
03 00000000`002ed8a0 000007fe`ac707de3 opencv_world400d!std::_Invoker_functor::_Call<std::vector<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc>,std::allocator<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc> > > (<function> ** _Obj = 0x00000000`020f85c8, class std::vector<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc>,std::allocator<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc> > > * <_Args_0> = 0x00000000`002edca8 { size=5 }, class std::vector<cv::GArg,std::allocator<cv::GArg> > * <_Args_1> = 0x00000000`020f8620 { size=5 })+0x89 [c:\program files (x86)\microsoft visual studio 14.0\vc\include\type_traits @ 1375] 
04 00000000`002ed920 000007fe`ac6fb0d2 opencv_world400d!std::invoke<std::vector<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc>,std::allocator<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc> > > (<function> ** _Obj = 0x00000000`020f85c8, class std::vector<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc>,std::allocator<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc> > > * <_Args_0> = 0x00000000`002edca8 { size=5 }, class std::vector<cv::GArg,std::allocator<cv::GArg> > * <_Args_1> = 0x00000000`020f8620 { size=5 })+0x83 [c:\program files (x86)\microsoft visual studio 14.0\vc\include\type_traits @ 1443] 
05 00000000`002ed970 000007fe`ac70cc5a opencv_world400d!std::_Invoke_ret<std::vector<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc>,std::allocator<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc> > >,std::vector<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc>,std::allocator<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc> > > (struct std::_Forced<std::vector<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc>,std::allocator<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc> > >,0> __formal = struct std::_Forced<std::vector<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc>,std::allocator<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc> > >,0>, <function> ** <_Vals_0> = 0x00000000`020f85c8, class std::vector<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc>,std::allocator<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc> > > * <_Vals_1> = 0x00000000`002edca8 { size=5 }, class std::vector<cv::GArg,std::allocator<cv::GArg> > * <_Vals_2> = 0x00000000`020f8620 { size=5 })+0x82 [c:\program files (x86)\microsoft visual studio 14.0\vc\include\type_traits @ 1468] 
06 00000000`002ed9c0 000007fe`ac818c97 opencv_world400d!std::_Func_impl<std::vector<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc>,std::allocator<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc> > > (class std::vector<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc>,std::allocator<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc> > > * <_Args_0> = 0x00000000`002edca8 { size=5 }, class std::vector<cv::GArg,std::allocator<cv::GArg> > * <_Args_1> = 0x00000000`020f8620 { size=5 })+0x8a [c:\program files (x86)\microsoft visual studio 14.0\vc\include\functional @ 212] 
07 00000000`002eda20 000007fe`ac8197e5 opencv_world400d!std::_Func_class<std::vector<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc>,std::allocator<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc> > >,std::vector<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc>,std::allocator<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc> > > const & __ptr64,std::vector<cv::GArg,std::allocator<cv::GArg> > const & __ptr64>::operator()(class std::vector<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc>,std::allocator<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc> > > * <_Args_0> = 0x00000000`002edca8 { size=5 }, class std::vector<cv::GArg,std::allocator<cv::GArg> > * <_Args_1> = 0x00000000`020f8620 { size=5 })+0xa7 [c:\program files (x86)\microsoft visual studio 14.0\vc\include\functional @ 279] 
08 00000000`002eda80 000007fe`ac7aeadf opencv_world400d!cv::gimpl::passes::inferMeta(struct ade::passes::PassContext * ctx = 0x00000000`002ee748, bool meta_is_initialized = false)+0x4f5 [c:\build\master_winpack-build-win64-vc14\opencv\modules\gapi\src\compiler\passes\meta.cpp @ 78] 
09 00000000`002ee340 000007fe`ac7b8c08 opencv_world400d!std::_Invoker_functor::_Call<void (<function> ** _Obj = 0x00000000`020ec440, struct ade::passes::PassContext * <_Args_0> = 0x00000000`002ee748, bool * <_Args_1> = 0x00000000`020ec448)+0x5f [c:\program files (x86)\microsoft visual studio 14.0\vc\include\type_traits @ 1377] 
0a 00000000`002ee380 000007fe`ac7b014c opencv_world400d!std::invoke<void (<function> ** _Obj = 0x00000000`020ec440, struct ade::passes::PassContext * <_Args_0> = 0x00000000`002ee748, bool * <_Args_1> = 0x00000000`020ec448)+0x68 [c:\program files (x86)\microsoft visual studio 14.0\vc\include\type_traits @ 1445] 
0b 00000000`002ee3c0 000007fe`ac7aef3c opencv_world400d!std::_Invoke_ret<void (struct std::_Forced<std::_Unforced,0> __formal = struct std::_Forced<std::_Unforced,0>, <function> ** <_Vals_0> = 0x00000000`020ec440, struct ade::passes::PassContext * <_Vals_1> = 0x00000000`002ee748, bool * <_Vals_2> = 0x00000000`020ec448)+0x6c [c:\program files (x86)\microsoft visual studio 14.0\vc\include\type_traits @ 1476] 
0c 00000000`002ee400 000007fe`ac7ae75c opencv_world400d!std::_Call_binder<std::_Unforced,0,1,void (struct std::_Forced<std::_Unforced,0> _Fr = struct std::_Forced<std::_Unforced,0>, struct std::integer_sequence<unsigned __int64,0,1> __formal = struct std::integer_sequence<unsigned __int64,0,1>, <function> ** _Obj = 0x00000000`020ec440, class std::tuple<std::_Ph<1>,bool> * _Tpl = 0x00000000`020ec448, class std::tuple<ade::passes::PassContext &> * _Ut = 0x00000000`002ee480 {...})+0x9c [c:\program files (x86)\microsoft visual studio 14.0\vc\include\functional @ 827] 
0d 00000000`002ee450 000007fe`ac7c6e9a opencv_world400d!std::_Binder<std::_Unforced,void (struct ade::passes::PassContext * <_Unbargs_0> = 0x00000000`002ee748)+0x7c [c:\program files (x86)\microsoft visual studio 14.0\vc\include\functional @ 881] 
0e 00000000`002ee4b0 000007fe`ac7d1089 opencv_world400d!ade::ExecutionEngine::PassWrapper<std::_Binder<std::_Unforced,void (struct ade::passes::PassContext * context = 0x00000000`002ee748)+0x14a [c:\build\master_winpack-build-win64-vc14\build\3rdparty\ade\ade-0.1.1d\sources\ade\include\ade\execution_engine\execution_engine.hpp @ 185] 
0f 00000000`002ee560 000007fe`ad40ab69 opencv_world400d!ade::detail::PassConceptImpl<ade::passes::PassContext,ade::ExecutionEngine::PassWrapper<std::_Binder<std::_Unforced,void (struct ade::passes::PassContext * context = 0x00000000`002ee748)+0x39 [c:\build\master_winpack-build-win64-vc14\build\3rdparty\ade\ade-0.1.1d\sources\ade\include\ade\passmanager.hpp @ 131] 
10 00000000`002ee590 000007fe`ad40ac92 opencv_world400d!ade::PassList<ade::passes::PassContext>::run(struct ade::passes::PassContext * context = 0x00000000`002ee748)+0xc9 [c:\build\master_winpack-build-win64-vc14\build\3rdparty\ade\ade-0.1.1d\sources\ade\include\ade\passmanager.hpp @ 153] 
11 00000000`002ee640 000007fe`ad40b47b opencv_world400d!ade::PassManager<ade::passes::PassContext>::run(struct ade::passes::PassContext * context = 0x00000000`002ee748)+0xb2 [c:\build\master_winpack-build-win64-vc14\build\3rdparty\ade\ade-0.1.1d\sources\ade\include\ade\passmanager.hpp @ 82] 
12 00000000`002ee6f0 000007fe`ac7d1103 opencv_world400d!ade::ExecutionEngine::runPasses(class ade::Graph * graph = 0x00000000`020ed4d0)+0x9b [c:\build\master_winpack-build-win64-vc14\build\3rdparty\ade\ade-0.1.1d\sources\ade\source\execution_engine.cpp @ 116] 
13 00000000`002ee7f0 000007fe`ac7cd73b opencv_world400d!cv::gimpl::GCompiler::runPasses(class ade::Graph * g = 0x00000000`020ed4d0)+0x63 [c:\build\master_winpack-build-win64-vc14\opencv\modules\gapi\src\compiler\gcompiler.cpp @ 229] 
14 00000000`002ee990 000007fe`ac6ef8ef opencv_world400d!cv::gimpl::GCompiler::compile(void)+0x5b [c:\build\master_winpack-build-win64-vc14\opencv\modules\gapi\src\compiler\gcompiler.cpp @ 279] 
15 00000000`002ee9e0 000007fe`ac6ed80f opencv_world400d!cv::GComputation::compile(class std::vector<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc>,std::allocator<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc> > > * metas = 0x00000000`002eeca8 { size=0 }, class std::vector<cv::GCompileArg,std::allocator<cv::GCompileArg> > * args = 0x00000000`002ef698 { size=0 })+0x9f [c:\build\master_winpack-build-win64-vc14\opencv\modules\gapi\src\api\gcomputation.cpp @ 76] 
16 00000000`002eec50 000007fe`ac6ee2cb opencv_world400d!cv::GComputation::apply(class std::vector<cv::util::variant<cv::Mat,cv::Scalar_<double>,cv::UMat,cv::gapi::own::Mat,cv::gapi::own::Scalar,cv::detail::VectorRef>,std::allocator<cv::util::variant<cv::Mat,cv::Scalar_<double>,cv::UMat,cv::gapi::own::Mat,cv::gapi::own::Scalar,cv::detail::VectorRef> > > * ins = 0x00000000`002eed70 { size=1 }, class std::vector<cv::util::variant<cv::Mat *,cv::Scalar_<double> *,cv::UMat *,cv::gapi::own::Mat *,cv::gapi::own::Scalar *,cv::detail::VectorRef>,std::allocator<cv::util::variant<cv::Mat *,cv::Scalar_<double> *,cv::UMat *,cv::gapi::own::Mat *,cv::gapi::own::Scalar *,cv::detail::VectorRef> > > * outs = 0x00000000`002eed50 { size=1 }, class std::vector<cv::GCompileArg,std::allocator<cv::GCompileArg> > * args = 0x00000000`002ef698 { size=0 })+0x16f [c:\build\master_winpack-build-win64-vc14\opencv\modules\gapi\src\api\gcomputation.cpp @ 116] 
17 00000000`002eed30 00000001`3f423baa opencv_world400d!cv::GComputation::apply(class cv::Mat * in = 0x00000000`002ef6d8, class cv::Mat * out = 0x00000000`002ef070, class std::vector<cv::GCompileArg,std::allocator<cv::GCompileArg> > * args = 0x00000000`002ef698 { size=0 })+0xbb [c:\build\master_winpack-build-win64-vc14\opencv\modules\gapi\src\api\gcomputation.cpp @ 140] 
18 00000000`002eedd0 00000001`3f424954 testGapi!main(int argc = 0n1, char ** argv = 0x00000000`020b8b30)+0x43a [c:\temp\testgapi\testgapi\testgapi.cpp @ 36] 
19 00000000`002ef850 00000001`3f4247f7 testGapi!invoke_main(void)+0x34 [f:\dd\vctools\crt\vcstartup\src\startup\exe_common.inl @ 65] 
1a 00000000`002ef890 00000001`3f4246be testGapi!__scrt_common_main_seh(void)+0x127 [f:\dd\vctools\crt\vcstartup\src\startup\exe_common.inl @ 253] 
1b 00000000`002ef8f0 00000001`3f424979 testGapi!__scrt_common_main(void)+0xe [f:\dd\vctools\crt\vcstartup\src\startup\exe_common.inl @ 296] 
1c 00000000`002ef920 00000000`77ba59cd testGapi!mainCRTStartup(void)+0x9 [f:\dd\vctools\crt\vcstartup\src\startup\exe_main.cpp @ 17] 
1d 00000000`002ef950 00000000`77d0383d kernel32!BaseThreadInitThunk+0xd
1e 00000000`002ef980 00000000`00000000 ntdll!RtlUserThreadStart+0x1d

```



GMat

# What is GMatDesc

It describe the shape of a Mat instance, eg

```cpp
0:000> dt -b in
Local var @ 0x2ed6f8 Type cv::GMatDesc*
0x00000000`002ed7e0
   +0x000 depth            : 0n0
   +0x004 chan             : 0n3
   +0x008 size             : cv::gapi::own::Size
      +0x000 width            : 0n512
      +0x004 height           : 0n512
```



What is 

# How to understand MetaHelper<>?

From code

```cpp
    template<typename K, typename... Ins, typename Out>
    struct MetaHelper<K, std::tuple<Ins...>, Out >
    {
        template<int... IIs>
        static GMetaArgs getOutMeta_impl(const GMetaArgs &in_meta,
                                         const GArgs &in_args,
                                         detail::Seq<IIs...>)
        {
            // FIXME: decay?
            using R = typename MetaType<Out>::type;
            const R r = K::outMeta( get_in_meta<Ins>(in_meta, in_args, IIs)... );
            return GMetaArgs{ GMetaArg(r) };
        }
        // FIXME: help users identify how outMeta must look like (via default impl w/static_assert?)

        static GMetaArgs getOutMeta(const GMetaArgs &in_meta,
                                    const GArgs &in_args)
        {
            return getOutMeta_impl(in_meta,
                                   in_args,
                                   typename detail::MkSeq<sizeof...(Ins)>::type());
        }
    };

```

From debugger the definition is 

```cpp
opencv_world400d!cv::detail::MetaHelper{
	cv::gapi::core::GResize,	// typename K
	std::tuple{cv::GMat,cv::Size_{int},double,double,int}, // typename... Ins
	cv::GMat}	// typename Out
```



# What is GMetaArgs and GArgs?

GMetaArgs &in_meta

```cpp
std::vector<
	cv::util::variant<
		cv::util::monostate,
		cv::GMatDesc,
		cv::GScalarDesc,
		cv::GArrayDesc
		>,
	std::allocator<cv::util::variant<cv::util::monostate,cv::GMatDesc,cv::GScalarDesc,cv::GArrayDesc> > 
> *	
```

GArgs

```cpp
std::vector<cv::GArg,std::allocator<cv::GArg> > *
```

# GScalarDesc

It's empty

```cpp
//N:\3rd_sw\OpenCV\4.0\build\include\opencv2\gapi\gscalar.hpp
struct GScalarDesc
{
    // NB.: right now it is empty

    inline bool operator== (const GScalarDesc &) const
    {
        return true; // NB: implement this method if GScalar meta appears
    }

    inline bool operator!= (const GScalarDesc &rhs) const
    {
        return !(*this == rhs);
    }
};
```

# GArrayDesc

It's empty

```cpp
struct GArrayDesc
{
    // FIXME: Body
    // FIXME: Also implement proper operator== then
    bool operator== (const GArrayDesc&) const { return true; }
};
```

# GArg

It just stores a `any`

```cpp
class GAPI_EXPORTS GArg
{    
	util::any value;
};
```

# how is `GCPUResize` called

callstack:



```cpp
0:000> kpn
 # Child-SP          RetAddr           Call Site
00 00000000`002ecfc8 000007fe`af15a005 opencv_world400d!GCPUResize::run(class cv::Mat * in = 0x00000000`002ed170, class cv::Size_<int> * sz = 0x00000000`002ed168, double fx = 1.5159198822462797566e-317, double fy = 1.5159159297211130267e-317, int interp = 0n3068128, class cv::Mat * out = 0x00000002`42ff4010) [c:\build\master_winpack-build-win64-vc14\opencv\modules\gapi\src\backends\cpu\gcpucore.cpp @ 459] 
01 00000000`002ecfd0 000007fe`af1604ac opencv_world400d!cv::detail::OCVCallHelper<GCPUResize,std::tuple<cv::GMat,cv::Size_<int>,double,double,int>,std::tuple<cv::GMat> >::call_and_postprocess<cv::Mat,cv::Size_<int>,double,double,int>::call<cv::detail::tracked_cv_mat>(class cv::Mat * <ins_0> = 0x00000000`002ed080, class cv::Size_<int> * <ins_1> = 0x00000000`002ed170, double * <ins_2> = 0x00000000`002ed168, double * <ins_3> = 0x00000000`002ed160, int * <ins_4> = 0x00000000`002ed158, struct cv::detail::tracked_cv_mat * <outs_0> = 0x00000000`002ed0e0)+0xe5 [c:\build\master_winpack-build-win64-vc14\opencv\modules\gapi\include\opencv2\gapi\cpu\gcpukernel.hpp @ 224] 
02 00000000`002ed050 000007fe`af16d7d3 opencv_world400d!cv::detail::OCVCallHelper<GCPUResize,std::tuple<cv::GMat,cv::Size_<int>,double,double,int>,std::tuple<cv::GMat> >::call_impl<0,1,2,3,4,0>(class cv::GCPUContext * ctx = 0x00000000`002ed6b0, struct cv::detail::Seq<0,1,2,3,4> __formal = struct cv::detail::Seq<0,1,2,3,4>, struct cv::detail::Seq<0> __formal = struct cv::detail::Seq<0>)+0x15c [c:\build\master_winpack-build-win64-vc14\opencv\modules\gapi\include\opencv2\gapi\cpu\gcpukernel.hpp @ 237] 
03 00000000`002ed1c0 000007fe`af1484e3 opencv_world400d!cv::detail::OCVCallHelper<GCPUResize,std::tuple<cv::GMat,cv::Size_<int>,double,double,int>,std::tuple<cv::GMat> >::call(class cv::GCPUContext * ctx = 0x00000000`002ed6b0)+0x33 [c:\build\master_winpack-build-win64-vc14\opencv\modules\gapi\include\opencv2\gapi\cpu\gcpukernel.hpp @ 245] 
04 00000000`002ed200 000007fe`af150e0c opencv_world400d!std::_Invoker_functor::_Call<void (<function> ** _Obj = 0x00000000`002ed658, class cv::GCPUContext * <_Args_0> = 0x00000000`002ed6b0)+0x43 [c:\program files (x86)\microsoft visual studio 14.0\vc\include\type_traits @ 1377] 
05 00000000`002ed240 000007fe`af148750 opencv_world400d!std::invoke<void (<function> ** _Obj = 0x00000000`002ed658, class cv::GCPUContext * <_Args_0> = 0x00000000`002ed6b0)+0x4c [c:\program files (x86)\microsoft visual studio 14.0\vc\include\type_traits @ 1445] 
06 00000000`002ed280 000007fe`af151b11 opencv_world400d!std::_Invoke_ret<void,void (struct std::_Forced<void,1> __formal = struct std::_Forced<void,1>, <function> ** <_Vals_0> = 0x00000000`002ed658, class cv::GCPUContext * <_Vals_1> = 0x00000000`002ed6b0)+0x50 [c:\program files (x86)\microsoft visual studio 14.0\vc\include\type_traits @ 1462] 
07 00000000`002ed2c0 000007fe`af147540 opencv_world400d!std::_Func_impl<void (class cv::GCPUContext * <_Args_0> = 0x00000000`002ed6b0)+0x51 [c:\program files (x86)\microsoft visual studio 14.0\vc\include\functional @ 214] 
08 00000000`002ed300 000007fe`af147678 opencv_world400d!std::_Func_class<void,cv::GCPUContext & __ptr64>::operator()(class cv::GCPUContext * <_Args_0> = 0x00000000`002ed6b0)+0x70 [c:\program files (x86)\microsoft visual studio 14.0\vc\include\functional @ 280] 
09 00000000`002ed340 000007fe`af145d79 opencv_world400d!cv::GCPUKernel::apply(class cv::GCPUContext * ctx = 0x00000000`002ed6b0)+0x68 [c:\build\master_winpack-build-win64-vc14\opencv\modules\gapi\src\backends\cpu\gcpukernel.cpp @ 52] 
0a 00000000`002ed370 000007fe`af1293f6 opencv_world400d!cv::gimpl::GCPUExecutable::run(class std::vector<std::pair<cv::gimpl::RcDesc,cv::util::variant<cv::Mat,cv::Scalar_<double>,cv::UMat,cv::gapi::own::Mat,cv::gapi::own::Scalar,cv::detail::VectorRef> >,std::allocator<std::pair<cv::gimpl::RcDesc,cv::util::variant<cv::Mat,cv::Scalar_<double>,cv::UMat,cv::gapi::own::Mat,cv::gapi::own::Scalar,cv::detail::VectorRef> > > > * input_objs = 0x00000000`002ee3a8 { size=1 }, class std::vector<std::pair<cv::gimpl::RcDesc,cv::util::variant<cv::Mat *,cv::Scalar_<double> *,cv::UMat *,cv::gapi::own::Mat *,cv::gapi::own::Scalar *,cv::detail::VectorRef> >,std::allocator<std::pair<cv::gimpl::RcDesc,cv::util::variant<cv::Mat *,cv::Scalar_<double> *,cv::UMat *,cv::gapi::own::Mat *,cv::gapi::own::Scalar *,cv::detail::VectorRef> > > > * output_objs = 0x00000000`002ee3e8 { size=1 })+0x6a9 [c:\build\master_winpack-build-win64-vc14\opencv\modules\gapi\src\backends\cpu\gcpubackend.cpp @ 210] 
0b 00000000`002eddb0 000007fe`af0a436f opencv_world400d!cv::gimpl::GExecutor::run(struct cv::gimpl::GRuntimeArgs * args = 0x00000000`002eebb0)+0xb06 [c:\build\master_winpack-build-win64-vc14\opencv\modules\gapi\src\executor\gexecutor.cpp @ 213] 
0c 00000000`002eeb50 000007fe`af0a2fd7 opencv_world400d!cv::GCompiled::Priv::run(struct cv::gimpl::GRuntimeArgs * args = 0x00000000`002eebb0)+0x5f [c:\build\master_winpack-build-win64-vc14\opencv\modules\gapi\src\compiler\gcompiled.cpp @ 39] 
0d 00000000`002eeb90 000007fe`aefbd8d3 opencv_world400d!cv::GCompiled::operator()(class std::vector<cv::util::variant<cv::Mat,cv::Scalar_<double>,cv::UMat,cv::gapi::own::Mat,cv::gapi::own::Scalar,cv::detail::VectorRef>,std::allocator<cv::util::variant<cv::Mat,cv::Scalar_<double>,cv::UMat,cv::gapi::own::Mat,cv::gapi::own::Scalar,cv::detail::VectorRef> > > * ins = 0x00000000`002eed30 { size=0 }, class std::vector<cv::util::variant<cv::Mat *,cv::Scalar_<double> *,cv::UMat *,cv::gapi::own::Mat *,cv::gapi::own::Scalar *,cv::detail::VectorRef>,std::allocator<cv::util::variant<cv::Mat *,cv::Scalar_<double> *,cv::UMat *,cv::gapi::own::Mat *,cv::gapi::own::Scalar *,cv::detail::VectorRef> > > * outs = 0x00000000`002eed10 { size=0 })+0x87 [c:\build\master_winpack-build-win64-vc14\opencv\modules\gapi\src\compiler\gcompiled.cpp @ 95] 
0e 00000000`002eec10 000007fe`aefbe2cb opencv_world400d!cv::GComputation::apply(class std::vector<cv::util::variant<cv::Mat,cv::Scalar_<double>,cv::UMat,cv::gapi::own::Mat,cv::gapi::own::Scalar,cv::detail::VectorRef>,std::allocator<cv::util::variant<cv::Mat,cv::Scalar_<double>,cv::UMat,cv::gapi::own::Mat,cv::gapi::own::Scalar,cv::detail::VectorRef> > > * ins = 0x00000000`002eed30 { size=0 }, class std::vector<cv::util::variant<cv::Mat *,cv::Scalar_<double> *,cv::UMat *,cv::gapi::own::Mat *,cv::gapi::own::Scalar *,cv::detail::VectorRef>,std::allocator<cv::util::variant<cv::Mat *,cv::Scalar_<double> *,cv::UMat *,cv::gapi::own::Mat *,cv::gapi::own::Scalar *,cv::detail::VectorRef> > > * outs = 0x00000000`002eed10 { size=0 }, class std::vector<cv::GCompileArg,std::allocator<cv::GCompileArg> > * args = 0x00000000`002ef658 { size=0 })+0x233 [c:\build\master_winpack-build-win64-vc14\opencv\modules\gapi\src\api\gcomputation.cpp @ 120] 
0f 00000000`002eecf0 00000001`3f8b3baa opencv_world400d!cv::GComputation::apply(class cv::Mat * in = 0x00000000`002ef698, class cv::Mat * out = 0x00000000`002ef030, class std::vector<cv::GCompileArg,std::allocator<cv::GCompileArg> > * args = 0x00000000`002ef658 { size=0 })+0xbb [c:\build\master_winpack-build-win64-vc14\opencv\modules\gapi\src\api\gcomputation.cpp @ 140] 
10 00000000`002eed90 00000001`3f8b4954 testGapi!main(int argc = 0n1, char ** argv = 0x00000000`0207a010)+0x43a [c:\temp\testgapi\testgapi\testgapi.cpp @ 36] 
11 00000000`002ef810 00000001`3f8b47f7 testGapi!invoke_main(void)+0x34 [f:\dd\vctools\crt\vcstartup\src\startup\exe_common.inl @ 65] 
12 00000000`002ef850 00000001`3f8b46be testGapi!__scrt_common_main_seh(void)+0x127 [f:\dd\vctools\crt\vcstartup\src\startup\exe_common.inl @ 253] 
13 00000000`002ef8b0 00000001`3f8b4979 testGapi!__scrt_common_main(void)+0xe [f:\dd\vctools\crt\vcstartup\src\startup\exe_common.inl @ 296] 
14 00000000`002ef8e0 00000000`77ba59cd testGapi!mainCRTStartup(void)+0x9 [f:\dd\vctools\crt\vcstartup\src\startup\exe_main.cpp @ 17] 
15 00000000`002ef910 00000000`77d0383d kernel32!BaseThreadInitThunk+0xd
16 00000000`002ef940 00000000`00000000 ntdll!RtlUserThreadStart+0x1d

```

callstack0c

```cpp
void cv::GComputation::apply(GRunArgs &&ins, GRunArgsP &&outs, GCompileArgs &&args)
{
    const auto in_metas = descr_of(ins);
    // FIXME Graph should be recompiled when GCompileArgs have changed
    if (m_priv->m_lastMetas != in_metas)
    {
        if (m_priv->m_lastCompiled &&
            m_priv->m_lastCompiled.canReshape() &&
            formats_are_same(m_priv->m_lastMetas, in_metas))
        {
            m_priv->m_lastCompiled.reshape(in_metas, args);
        }
        else
        {
            // FIXME: Had to construct temporary object as compile() takes && (r-value)
            m_priv->m_lastCompiled = compile(GMetaArgs(in_metas), std::move(args));
        }
        m_priv->m_lastMetas = in_metas;
    }
    m_priv->m_lastCompiled(std::move(ins), std::move(outs));
}

// 0b
void cv::gimpl::GExecutor::run(cv::gimpl::GRuntimeArgs &&args)
{
    // (2)
    const auto proto = m_gm.metadata().get<Protocol>();

    // Basic check if input/output arguments are correct
    // FIXME: Move to GCompiled (do once for all GExecutors)
    if (proto.inputs.size() != args.inObjs.size()) // TODO: Also check types
    {
        util::throw_error(std::logic_error
                          ("Computation's input protocol doesn\'t "
                           "match actual arguments!"));
    }
    if (proto.outputs.size() != args.outObjs.size()) // TODO: Also check types
    {
        util::throw_error(std::logic_error
                          ("Computation's output protocol doesn\'t "
                           "match actual arguments!"));
    }

    namespace util = ade::util;

    //ensure that output Mat parameters are correctly allocated
    for (auto index : util::iota(proto.out_nhs.size()) )     //FIXME: avoid copy of NodeHandle and GRunRsltComp ?
    {
        auto& nh = proto.out_nhs.at(index);
        const Data &d = m_gm.metadata(nh).get<Data>();
        if (d.shape == GShape::GMAT)
        {
            using cv::util::get;
            const auto desc = get<cv::GMatDesc>(d.meta);
            const auto type = CV_MAKETYPE(desc.depth, desc.chan);

#if !defined(GAPI_STANDALONE)
            // Building as part of OpenCV - follow OpenCV behavior
            // if output buffer is not enough to hold the result, reallocate it
            auto& out_mat   = *get<cv::Mat*>(args.outObjs.at(index));
            out_mat.create(cv::gapi::own::to_ocv(desc.size), type);
#else
            // Building standalone - output buffer should always exist,
            // and _exact_ match our inferred metadata
            auto& out_mat   = *get<cv::gapi::own::Mat*>(args.outObjs.at(index));
            GAPI_Assert(   out_mat.type() == type
                        && out_mat.data   != nullptr
                        && out_mat.rows   == desc.size.height
                        && out_mat.cols   == desc.size.width)
#endif // !defined(GAPI_STANDALONE)
        }
    }
    // Update storage with user-passed objects
    for (auto it : ade::util::zip(ade::util::toRange(proto.inputs),
                                  ade::util::toRange(args.inObjs)))
    {
        magazine::bindInArg(m_res, std::get<0>(it), std::get<1>(it));
    }
    for (auto it : ade::util::zip(ade::util::toRange(proto.outputs),
                                  ade::util::toRange(args.outObjs)))
    {
        magazine::bindOutArg(m_res, std::get<0>(it), std::get<1>(it));
    }

    // Reset internal data
    for (auto &sd : m_slots)
    {
        const auto& data = m_gm.metadata(sd.data_nh).get<Data>();
        magazine::resetInternalData(m_res, data);
    }

    // Run the script
    for (auto &op : m_ops)
    {
        // (5)
        using InObj  = GIslandExecutable::InObj;
        using OutObj = GIslandExecutable::OutObj;
        std::vector<InObj>  in_objs;
        std::vector<OutObj> out_objs;
        in_objs.reserve (op.in_objects.size());
        out_objs.reserve(op.out_objects.size());

        for (const auto &rc : op.in_objects)
        {
            in_objs.emplace_back(InObj{rc, magazine::getArg(m_res, rc)});
        }
        for (const auto &rc : op.out_objects)
        {
            out_objs.emplace_back(OutObj{rc, magazine::getObjPtr(m_res, rc)});
        }

        // (6)
        op.isl_exec->run(std::move(in_objs), std::move(out_objs));
    }

    // (7)
    for (auto it : ade::util::zip(ade::util::toRange(proto.outputs),
                                  ade::util::toRange(args.outObjs)))
    {
        magazine::writeBack(m_res, std::get<0>(it), std::get<1>(it));
    }
}
```



# What is cv::gin

A: 

```cpp
void cv::GComputation::apply(cv::Mat in, cv::Mat &out, GCompileArgs &&args)
{
    apply(cv::gin(in), cv::gout(out), std::move(args));
    // FIXME: The following doesn't work!
    // Operation result is not replicated into user's object
    // apply({GRunArg(in)}, {GRunArg(out)});
}

// N:\3rd_sw\OpenCV\4.0\build\include\opencv2\gapi\garg.hpp
template<typename... Ts> inline GRunArgs gin(const Ts&... args)
{
    return GRunArgs{ GRunArg(detail::wrap_host_helper<Ts>::wrap_in(args))... };
}
```
