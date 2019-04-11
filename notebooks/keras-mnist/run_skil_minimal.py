from skil import Skil, WorkSpace, Experiment, Model, Deployment
from keras.datasets import mnist

# Initialize a new experiment in a workspace
skil_server = Skil()

work_space = WorkSpace(skil_server, name='mnist-workspace')
experiment = Experiment(work_space, name='mnist-experiment')

# Deploy a model with SKIL
deployment = Deployment(skil_server, name='mnist-deployment')

model = Model('model.h5', name='mnist-model', experiment=experiment)
service = model.deploy(deployment)

# Prediction
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_test = x_test.reshape(10000, 784)
x_test = x_test.astype('float32')
x_test /= 255

print(service.predict_single(x_test[0]))
print(service.predict(x_test[:10]))