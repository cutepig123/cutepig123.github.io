[TOC]

tensorflow keras analysis



code

```python
from keras.models import Sequential

model = Sequential()

from keras.layers import Dense

model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True))

# x_train and y_train are Numpy arrays --just like in the Scikit-Learn API.
model.fit(x_train, y_train, epochs=5, batch_size=32)

# Alternatively, you can feed batches to your model manually:
model.train_on_batch(x_batch, y_batch)

# Evaluate your performance in one line:

loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)

# Or generate predictions on new data:

classes = model.predict(x_test, batch_size=128)
```

# Q: where is Sequential defined?

A:  

From https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/keras/models.py



```python
from tensorflow.python.keras.engine import sequential
Sequential = sequential.Sequential  # pylint: disable=invalid-name

```

We get the definition of *Sequential* class From https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/keras/engine/sequential.py



```python
@keras_export('keras.models.Sequential', 'keras.Sequential')
class Sequential(training.Model):
   ...
def add(self, layer): 
    ...
   ...
     
        batch_shape, dtype = training_utils.get_input_shape_and_dtype(layer)
        if batch_shape:
          # Instantiate an input layer.
          x = input_layer.Input(
              batch_shape=batch_shape, dtype=dtype, name=layer.name + '_input')
          # This will build the current layer
          # and create the node connecting the current layer
          # to the input layer we just created.
          layer(x)
          set_inputs = True
```

# Q: where is compile()? 

```python
from tensorflow.python.keras.engine import training
```

we find the definition of Model class from file:https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/keras/engine/training.py

