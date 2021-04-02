[TOC]

g-api notes

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

A: because only when apply the input shape can be determined

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

# Q: How to impl a MergeChannel() operator?

A: ???



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