# Deploying a Keras model with SKIL in 60 seconds

## Start SKIL with docker

```bash
docker pull skymindops/skil-ce
docker run --rm -it -p 9008:9008 -p 8080:8080 skymindops/skil-ce bash /start-skil.sh
```

## Install Python SKIL client, train and persist a Keras model

```bash
git clone https://github.com/SkymindIO/skil-python
cd examples/keras-mnist-mlp
virtualenv venv && source venv/bin/activate
pip install skil tensorflow keras

python train.py
# OR
python train_minimal.py
```

## Deploy model with SKIL

* [run_skil_minimal.py](run_skil_minimal.py)
* Please see [run_skil_minimal.ipynb](run_skil_minimal.ipynb) notebook for more details

```python
from skil import Skil, WorkSpace, Experiment, Model, Deployment

skil_server = Skil()

work_space = WorkSpace(skil_server, name='mnist-workspace')
experiment = Experiment(work_space, name='mnist-experiment')
deployment = Deployment(skil_server, name='mnist-deployment')

model = Model('model.h5', name='mnist-model', experiment=experiment)
model.deploy(deployment)
```

# Working with existing deployments

**Prerequisites**: ``` pip install numpy matplotlib opencv-python jupyter```

* [run_skil_client.ipynb](run_skil_client.ipynb) notebook

```python
from skil import Skil, Service
from skil import get_workspace_by_id, get_experiment_by_id, get_model_by_id, get_deployment_by_id

skil_server = Skil()

work_space = get_workspace_by_id(skil_server, 'your_workspace_id')
experiment = get_experiment_by_id(work_space, 'your_experiment_id')
deployment = get_deployment_by_id(skil_server, 'your_deployment_id')
model = get_model_by_id(experiment, 'your_experiment_id')

service = Service(
    skil=skil_server,
    model=model,
    deployment=deployment,
    model_deployment=None
)

# Prediction
import cv2
import numpy as np

image = cv2.imread("images/mnist.jpg", cv2.IMREAD_GRAYSCALE)
image = np.squeeze(image.reshape(1,-1))

predicted = service.predict_single(image)
print('Predicted:',predicted)
print('Target Class:',np.argmax(predicted))
```