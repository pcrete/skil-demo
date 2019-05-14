from skil import Skil, Service, utils
from skil import get_workspace_by_id
from skil import get_experiment_by_id
from skil import get_model_by_id
from skil import get_deployment_by_id

from utils import annotate_image
from time import time
import cv2

skil_server = Skil(
    host      = 'localhost',
    port      = 9008,
    user_id   = 'admin',
    password  = 'Skymind'
)

experiment = skil_server.api.list_all_experiments(skil_server.server_id)[0]

workspace_id  = experiment.model_history_id
experiment_id = 'yolo-experiment-01'
model_id      = 'yolo-model-01'
deployment_id = '0'

work_space = get_workspace_by_id(skil_server, workspace_id)
experiment = get_experiment_by_id(work_space, experiment_id)
deployment = get_deployment_by_id(skil_server, deployment_id)
model = get_model_by_id(experiment, model_id)

service = Service(
    skil=skil_server,
    model=model,
    deployment=deployment,
    model_deployment=None
)



cap = cv2.VideoCapture()
cap.open("http://10.0.1.8:8080/video?.mjpeg")   
image = ''
while(True): 
   start = time()
   ret, frame = cap.read()


   # detection = service.detect_objects(frame, threshold=0.25)

   # frame = annotate_image(frame, detection)

   if cv2.waitKey(1) & 0xFF == ord('q'): break
   cv2.imshow('yolo', frame)
   print(time()-start)

cap.release()
cv2.destroyAllWindows()

