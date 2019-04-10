# Deploying a Keras model with SKIL in 60 seconds

## Code Structure
1. Model Training
	* [train.py](train.py)
	* [train_minimal.py](train_minimal.py)
2. SKIL Deployment
	* [deploy_skil.py](deploy_skil.py)
	* [deploy_skil_minimal.py](deploy_skil_minimal.py) or [deploy_skil_minimal.ipynb](deploy_skil_minimal.ipynb) notebook
3. SKIL Client
	* [run_skil_client.py](run_skil_client.py) or [run_skil_client.ipynb](run_skil_client.ipynb) notebook
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
```

## Deploy model with SKIL

* [deploy_skil_minimal.ipynb](deploy_skil_minimal.ipynb)

```python
from skil import Skil, WorkSpace, Experiment, Model, Deployment

skil_server = Skil()
work_space = WorkSpace(skil_server, name='keras-mnist')
experiment = Experiment(work_space, name='mnist-experiment')
model = Model('model.h5', name="keras-mnist", experiment=experiment)

deployment = Deployment(skil_server)

model.deploy(deployment)
```

## Run SKIL client

* [run_skil_client.ipynb](run_skil_client.ipynb)

```python
from skil import Skil, Service
from skil import get_workspace_by_id, get_experiment_by_id, get_model_by_id, get_deployment_by_id

import cv2
import numpy as np

workspace_id  = 'your workspace_id'
experiment_id = 'your experiment_id'
model_id      = 'your model_id'
deployment_id = 'your deployment_id'

skil_server = Skil()

work_space = get_workspace_by_id(skil_server, workspace_id)
experiment = get_experiment_by_id(work_space, experiment_id))
model = get_model_by_id(experiment, model_id)
model_deployment = skil_server.api.models(deployment_id=deployment_id)

service = Service(
    skil=skil_server,
    model=model,
    deployment=deployment,
    model_deployment=model_deployment
)

# Prediction
image = cv2.imread("images/mnist.jpg", cv2.IMREAD_GRAYSCALE)
image = np.squeeze(image.reshape(1,-1))
predicted = service.predict_single(image)
print('Predicted:',predicted)
print('Target Class:',np.argmax(predicted))
```
