[TOC]

# TODO

- [ ] Unify myGraph API
  - [ ] How to manage memory? Prefer similar to openCV::Mat, the reference counted object can manage its own lifetime
  - [ ] How GApi supports multiple output GMats?
- [ ] Implement a basic version. it can demo the usage
- [ ] Implement an optimized version with CSE, etc

# Existing libraries

- OpenVX: OpenVINO or AMD ovx 

- OpenCV [G-API](N:\3rd_sw\OpenCV\4.0\sources\modules\gapi\samples): a more user friendly API

- Intel TBB flow graph

# APIs

## OpenVX API

- [ ] Does openVX has multiple output nodes?
  - [x] Yes. It seperates "node" and "image", vx_image is parameters
- [x] Can it create one graph, but execute multiple times with feeding different parameters
  - [x] From the API, It seems is not possible

```cpp
 //vx_api.h
 VX_API_ENTRY vx_graph VX_API_CALL vxCreateGraph(vx_context context);
 VX_API_ENTRY vx_status VX_API_CALL vxVerifyGraph(vx_graph graph);
 VX_API_ENTRY vx_status VX_API_CALL vxProcessGraph(vx_graph graph);
 VX_API_ENTRY vx_image VX_API_CALL vxCreateVirtualImage(vx_graph graph, vx_uint32 width, vx_uint32 height, vx_df_image color);
 
 //vx_node.h
 VX_API_ENTRY vx_node VX_API_CALL vxColorConvertNode(vx_graph graph, vx_image input, vx_image output);

// example
vx_graph graph = vxCreateGraph(context);
vx_node node = vxColorConvertNode(graph, src, dst);

status = vxVerifyGraph(graph);
status = vxProcessGraph(graph);

vxReleaseNode(&node);
vxReleaseGraph(&graph);
```

- [ ] How vxColorConvertNode() implemented?

It first create the specified node, then fill input and output parameters to the node

```cpp
vxCreateNodeByStructure(vx_graph graph,
	vx_enum kernelenum,
	vx_reference params[],
	vx_uint32 num){
    ...;
    vxCreateGenericNode(graph, kernel);
    ...;
    vxSetParameterByIndex(node,...);
    
}
```



## G-API API

- [x] What's diff between tf.Variable, tf.placeholder, tf.Constant?
  - [x] Variable: For training. optimizer will update variable in every run
  - [ ] placeholder: arguments in run()



It looks like tensor flow

- GMat <--> tf.placeholder
- Mat <--> tf.Constant
- GComputation  <--> Session
- GComputation (ins, outs) <--> No direct correspondence. Session.run(outs, {placeholders})
- GComputation.apply (ins) <--> No direct correspondence. Session.run(outs, {placeholders})

```cpp
 //core.hpp
 GAPI_EXPORTS GMat resize(const GMat& src, const Size& dsize, double fx = 0, double fy = 0, int interpolation = INTER_LINEAR);
 
 //GComputation.hpp
 class GComputation{
    ...
     GComputation(GProtoInputArgs &&ins,
                  GProtoOutputArgs &&outs);             // Arg-to-arg overload
  void apply(GRunArgs &&ins, GRunArgsP &&outs, GCompileArgs &&args = {});
 ...
 }
```

## TBB function_nodes

```cpp
  graph g;
  broadcast_node<int> input(g);
  function_node<int,int> squarer( g, unlimited, square() );
  function_node<int,int> cuber( g, unlimited, cube() );
  join_node< tuple<int,int>, queueing > join( g );
  function_node<tuple<int,int>,int>
      summer( g, serial, sum(result) );

  make_edge( input, squarer );
  make_edge( input, cuber );
  auto &ports = join.input_ports();
  auto &p0 = get<0>(ports);
  make_edge( squarer, p0 );
  make_edge( cuber, get<1>( join.input_ports() ) );
  make_edge( join, summer );

  for (int i = 1; i <= 10; ++i)
      input.try_put(i);
  g.wait_for_all();
```

## TBB continue nodes

```cpp
    graph g;
    continue_node< continue_msg> hello( g,
      []( const continue_msg &) {
          cout << "Hello";
      }
    );
    continue_node< continue_msg> world( g,
      []( const continue_msg &) {
          cout << " World\n";
      }
    );
    make_edge(hello, world);
    hello.try_put(continue_msg());
    g.wait_for_all();
```

## Tensor flow

```python
# https://blog.gtwang.org/statistics/tensorflow-google-machine-learning-software-library-tutorial/

# define a model with variable initial values
W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b

init = tf.global_variables_initializer()
sess.run(init)

# run the model
print(sess.run(linear_model, {x:[1,2,3,4]}))

# test loss
y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))

# adjust weithging and then run again
fixW = tf.assign(W, [-1.])
fixb = tf.assign(b, [1.])
sess.run([fixW, fixb])
print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))

# training
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)
sess.run(init) # 將變數重設為錯誤的組合
for i in range(1000):
  sess.run(train, {x:[1,2,3,4], y:[0,-1,-2,-3]})
print(sess.run([W, b]))
```



## Tensor flow keras

```python
# https://www.tensorflow.org/guide/keras/overview

from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

model = tf.keras.Sequential([
# Adds a densely-connected layer with 64 units to the model:
layers.Dense(64, activation='relu', input_shape=(32,)),
# Add another:
layers.Dense(64, activation='relu'),
# Add a softmax layer with 10 output units:
layers.Dense(10, activation='softmax')])

model.compile(optimizer=tf.keras.optimizers.Adam(0.01),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# https://www.tensorflow.org/guide/keras/train_and_evaluate

# Train the model by slicing the data into "batches"
# of size "batch_size", and repeatedly iterating over
# the entire dataset for a given number of "epochs"
print('# Fit model on training data')
history = model.fit(x_train, y_train,
                    batch_size=64,
                    epochs=3,
                    # We pass some validation for
                    # monitoring validation loss and metrics
                    # at the end of each epoch
                    validation_data=(x_val, y_val))

# The returned "history" object holds a record
# of the loss values and metric values during training
print('\nhistory dict:', history.history)

# Evaluate the model on the test data using `evaluate`
print('\n# Evaluate on test data')
results = model.evaluate(x_test, y_test, batch_size=128)
print('test loss, test acc:', results)

# Generate predictions (probabilities -- the output of the last layer)
# on new data using `predict`
print('\n# Generate predictions for 3 samples')
predictions = model.predict(x_test[:3])
print('predictions shape:', predictions.shape)

# https://www.tensorflow.org/tutorials/quickstart/advanced
class MyModel(Model):
  def __init__(self):
    super(MyModel, self).__init__()
    self.conv1 = Conv2D(32, 3, activation='relu')
    self.flatten = Flatten()
    self.d1 = Dense(128, activation='relu')
    self.d2 = Dense(10, activation='softmax')

  def call(self, x):
    x = self.conv1(x)
    x = self.flatten(x)
    x = self.d1(x)
    return self.d2(x)

# Create an instance of the model
model = MyModel()
```

- [ ] AutoGraph  [the guide](https://www.tensorflow.org/guide/function).
- [ ] How is it implemented?

# Comparison

|                    | Reuse graph: a created graph can be used multiple times by feeding different inputs | CSE: common-subexpression elimination | partial inputs | switching back-ends | TODO                                      |
| ------------------ | ------------------------------------------------------------ | ------------------------------------- | -------------- | ------------------- | ----------------------------------------- |
| OpenVX             | x                                                            | x                                     | x              | v                   |                                           |
| G-API              | v                                                            | x                                     | x              | v                   |                                           |
| TBB function_nodes | v                                                            | x                                     | v              | x                   | How to make the graph configurable?<br /> |
| TBB continue_nodes | v                                                            | x                                     | v              | x                   | How to manage function arguments?         |
| tensorflow         |                                                              |                                       |                |                     |                                           |
|                    |                                                              |                                       |                |                     |                                           |
|                    |                                                              |                                       |                |                     |                                           |
|                    |                                                              |                                       |                |                     |                                           |

