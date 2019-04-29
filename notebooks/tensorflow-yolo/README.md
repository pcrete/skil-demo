# Object Detection with YOLO2

This example is meant to show off raw TF model import into SKIL 1.0.2. We've chosen object detection in computer vision as the application we want to demo in the context of Tensor Flow model import on SKIL. For the purposes of demoing computer vision on SKIL, we'll use a YOLO network for object deteciton as the application. The original YOLO2 model is in the darknet framework format, but fortunately we have a way of converting this format to the tensor flow format.

**The purpose of this demo on SKIL is two-fold:**
1. show off the native TensorFlow model import capabilities of the SKIL platform
2. show off a live real-world computer vision object detection demo on the SKIL platform


## Demo Workflow
* Start up SKIL Server
* Download the TensorFlow YOLOv2 model pre-trained on COCO from our  [dl4j-test resources here](https://github.com/deeplearning4j/dl4j-test-resources/blob/681a0cf2e9edb62c88a5dc41f7516e3b1dff3f19/src/main/resources/tf_graphs/examples/yolov2_608x608/frozen_model.pb) (Make sure to save this model as `yolo2.pb` in this folder)
* Import the model into the SKIL Model Server
* Run the YOLO2 Client from the local command line or python client

## Working with the YOLO Model

![alt text](https://pjreddie.com/media/image/model2.png "Image Courtesy of YOLO Website")

YOLO is a deep network for real-time object detection and classification. 
Paper: 
1. [You Only Look Once: Unified, Real-Time Object Detection](https://arxiv.org/pdf/1506.02640.pdf)
2. [YOLO9000: Better, Faster, Stronger 2](https://arxiv.org/pdf/1612.08242.pdf)

The specific version of the YOLO model that we use in this example is based on the YOLOv2 architecture was trained on the [COCO dataset](http://cocodataset.org/#home) and can recognize [80 distinct classes](https://github.com/pjreddie/darknet/blob/master/data/coco.names).

## Import the TensorFlow Protobuff File into the SKIL Model Server

Now we can log into SKIL and import the TensorFlow protobuff (.pb) file we created in the previous step.

1. Log into SKIL
2. Select the "**deployments**" option on the left side toolbar
3. Click on the "**New Deployment**" button
4. In the models section of the newly created deployment screen, select "**Import**" and locate the .pb file we created previously
5. For the placeholders options:
   * Names of the **Input** Placeholders: "input" (make sure to press 'enter' after you enter the name)
   * Names of the **Output** Placeholders: "output" (also make sure to press 'enter' after you enter the name)
6. Click on "**Import Model"** 
7. Click the "**start**" button on the endpoint

It will take a few seconds for the page to report that the endpoint has successfully started. Once the page lists the endpoint as running, however, you will have access to the model from the listed endpoint on the page. The endpoint URI will look something like: http://localhost:9008/endpoints/tf2/model/yolo/default/

Now we need a client application to query this endpoint and get object detection predictions.

## Getting started

### Python Client

#### Run YOLO-v2 Detection Inference¶
```python

import skil, requests, cv2, json
import numpy as np

# set configurations & temp image
threshold=0.5
needs_preprocessing=False
image_path='images/img-3.jpg'

url = 'http://{}/endpoints/{}/model/{}/v{}/detectobjects'.format(
    skil_server.config.host,
    deployment.name,
    model.name,
    model.version
)

response   = requests.post(
    url    = url,
    headers= skil_server.auth_headers,
    files  = {'file': open(image_path,'rb').read()},
    data   = {
        'id': model.id,
        'needs_preprocessing':needs_preprocessing,
        'threshold': threshold
    }
)
detections = response.json()
```

#### Detection JSON object
```json
{
    "height": 290.0,
    "predictedClasses": [
        "person",
        "horse",
        "umbrella",
        "handbag",
        "teddy bear",
        "dog",
        "elephant",
        "bottle",
        "backpack",
        "chair"
    ],
    "width": 105.0,
    "confidences": [
        0.9984509,
        0.0003896143,
        0.00022168506,
        0.00016007567,
        0.00012121937,
        6.202207e-05,
        3.9783445e-05,
        3.6805603e-05,
        3.272282e-05,
        3.252795e-05
    ],
    "centerY": 377.0,
    "centerX": 253.0,
    "predictedClassNumbers": [
        0,
        17,
        25,
        26,
        77,
        16,
        20,
        39,
        24,
        56
    ]
}
```

###  Java Client
Clone this repo with the command to get the included YOLOv2 sample application that will retrive predictions and render the bounding boxes locally:
```
git clone git@github.com:SkymindIO/SKIL_Examples.git

# build the jar
cd skil_yolo2_app/client_app
mvn package
```

This will build a jar named "skil-example-yolo2-tf-1.0.0.jar" in the ./target subdirectory of the client_app/ subdirectory.

```bash
# An example of this command in usage would be:
java -jar ./target/skil-example-yolo2-tf-1.0.0.jar --input [image URI] --endpoint [SKIL Endpoint URI]

# from an image
java -jar ./target/skil-example-yolo2-tf-1.0.0.jar \
--input https://raw.githubusercontent.com/tejaslodaya/car-detection-yolo/master/images/0012.jpg \
--endpoint http://localhost:9008/endpoints/tf2/model/yolo/default/

# from a webcam:
java -jar ./target/skil-example-yolo2-tf-1.0.0.jar \
--camera 0 \
--endpoint http://localhost:9008/endpoints/tf2/model/yolo/default/
```

where

* `--input` can be any input image you choose (local file with the file:// prefix, or an image file via an internet URI with a http:// prefix)
* `--endpoint` parameter is the endpoint you create when you import the TF .pb file
* `--camera` can be any camera device number starting from 0

## References:
* [SKIL_Examples/YOLO-object-detection-app](https://github.com/SkymindIO/SKIL_Examples/tree/master/YOLO-object-detection-app)
* [skil-python/examples/tensorflow-yolo](https://github.com/SkymindIO/skil-python/tree/master/examples/tensorflow-yolo)