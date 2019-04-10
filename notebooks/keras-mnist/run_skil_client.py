from skil import Skil, Service
from skil import get_workspace_by_id, get_experiment_by_id, get_model_by_id, get_deployment_by_id

import cv2
import numpy as np

workspace_id  = 'your workspace_id'
experiment_id = 'your experiment_id'
model_id      = 'your model_id'
deployment_id = 'your deployment_id'

skil_server = Skil(
    host='localhost',
    port=9008,
    user_id='your username',
    password='your password'
)

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