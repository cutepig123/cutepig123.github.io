---
categories: vision
---
如何训练自己的object detection model

# 目的

写一个找你妹机器人

# QA

## https://machinelearningmastery.com/how-to-train-an-object-detection-model-with-keras/

如何利用已有的模型，训练一个找袋鼠的模型？

| 12   | # define the modelmodel = MaskRCNN(mode='training', model_dir='./', config=config) |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

接下来，可以加载预定义的模型架构和权重。这可以通过在模型上调用*load_weights（）*函数并指定下载的“ *mask_rcnn_coco.h5* ”文件的路径来实现。

尽管将删除类特定的输出层，以便可以定义和训练新的输出层，但是该模型将按原样使用。这可以通过指定' *exclude* '参数并列出所有输出层以在加载模型后从模型中排除或删除来完成。这包括分类标签，边界框和蒙版的输出层。

| 12   | # load weights (mscoco)model.load_weights('mask_rcnn_coco.h5', by_name=True, exclude=["mrcnn_class_logits", "mrcnn_bbox_fc", "mrcnn_bbox", "mrcnn_mask"]) |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

接下来，可以通过调用*train（）*函数并传入训练数据集和验证数据集来将模型拟合到训练数据集上。我们还可以将学习率指定为配置中的默认学习率（0.001）。

我们还可以指定要训练的层。在这种情况下，**我们将只训练头部，即模型的输出层**。

| 12   | # train weights (output layers or 'heads')<br />model.train(train_set, test_set, learning_rate=config.LEARNING_RATE, epochs=5, ==layers='heads'==) |
| ---- | ------------------------------------------------------------ |
|      |                                                              |

我们可以通过进一步调整模型中所有权重的时期来进行此训练。这可以通过使用较小的学习率并将“层”参数从“正面”更改为“全部”来实现。

即使使用现代硬件，也可能需要花费一些时间才能在CPU上执行。我建议使用GPU运行代码，例如在[Amazon EC2上](https://machinelearningmastery.com/develop-evaluate-large-deep-learning-models-keras-amazon-web-services/)，**在P3型硬件上将在大约五分钟内完成代码**。

## https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html

https://blog.roboflow.com/train-a-tensorflow2-object-detection-model/

https://towardsdatascience.com/how-to-train-your-own-object-detector-with-tensorflows-object-detector-api-bec72ecfe1d9

https://www.google.com/search?q=how+to+train+a+object+detection+model&oq=how+to+train+a+objec&aqs=chrome.0.0i19j69i57j0i8i19i30.11894j0j4&sourceid=chrome&ie=UTF-8

## 迁移学习?