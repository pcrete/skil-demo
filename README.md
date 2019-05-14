# SKIL: Skymind Intelligence Layer

This project is introduced in an attempt to demonstrate the use of original repo here: https://github.com/SkymindIO/skil-python

## MLOps - Deep Learning in Production

<img src="docs/skil.png" width="800" />

<img src="docs/skil-1.png" width="815" />

## Installation


### 1. SKIL's docker image
To install SKIL itself, head over to [docs.skymind.ai](https://docs.skymind.ai/docs/docker-image). 

#### Skymind/skil

[https://hub.docker.com/r/skymind/skil/](https://hub.docker.com/r/skymind/skil/)
```bash
# pull the SKIL image
docker pull skymind/skil
docker pull skymind/skil:1.2.1-cpu-spark1.6-python2-centos7 
docker pull skymind/skil:1.2.1-cuda10.0-spark1.6-python2-centos7 
docker pull skymind/skil:1.2.1-cuda10.0-spark1.6-python2-ubuntu16.04
docker pull skymind/skil:1.2.1-cuda10.0-spark1.6-python2-ubuntu18.04

# run the SKIL server
docker run --rm -it -p 9008:9008 -p 8080:8080 skymind/skil

# or with gpu
docker run --runtime=nvidia --rm -it -p 9008:9008 -p 8080:8080 skymind/skil

# persistent data
docker volume create --name skil-data
docker volume create --name skil-conf
docker volume create --name skil-root

docker run -it --rm \
-v skil-root:/opt/skil \
-v skil-data:/var/skil \
-v skil-conf:/etc/skil \
-p 9008:9008 -p 8080:8080 \
skymind/skil:1.2.1-cpu-spark1.6-python2-centos7 

# add license file
-v /home/poom/.skil/skil-license.txt:/etc/skil/license.txt
```

#### SKIL environment variables for GPU mode

* [https://docs.skymind.ai/docs/skil-environment-ui](https://docs.skymind.ai/docs/skil-environment-ui)
* [https://docs.skymind.ai/docs/gpu-mode](https://docs.skymind.ai/docs/gpu-mode)

Sample Configuration:
```zsh
FORCE_APPLY_CONF=true

SKIL_CLASS_PATH=/opt/skil/cuda/*:/opt/skil/lib/*:/opt/skil/native/*:/etc/skil/*
SKIL_BACKEND=gpu

DEFAULT_ZEPPELIN_BACKEND=gpu
DEFAULT_ZEPPELIN_JVM_ARGS=-Xmx16g -Dorg.bytedeco.javacpp.maxbytes=16G -Dorg.bytedeco.javacpp.maxphysicalbytes=16G -Dorg.nd4j.versioncheck=false -Dorg.deeplearning4j.config.custom.enabled=false
```

Add ENV file to `/etc/skil/skil-env.sh`

```bash
# persistent data + gpu + env
docker run --runtime=nvidia --rm -it --network host \
-v skil-root:/opt/skil \
-v skil-data:/var/skil \
-v skil-conf:/etc/skil \
-v /home/skymind/skil-env.sh:/etc/skil/skil-env.sh \
skymind/skil:1.2.1-cuda10.0-spark1.6-python2-ubuntu16.04

# debug skil
tail -f /var/log/skil/skil.log
```

Now, you can access the SKIL UI by opening a browser window to [http://localhost:9008](http://localhost:9008) 

#### Skymindops/skil-ce
[https://hub.docker.com/r/skymindops/skil-ce](https://hub.docker.com/r/skymindops/skil-ce)

For more details, head over to: [docs/skil-ce_installation.md](docs/skil-ce_installation.md)


### Docker Commands

```bash
# expose all the container ports
docker run --network host ...
docker exec -i -t container_id bash
```


#### Nvidia-docker
* [Nvidia-docker](https://github.com/NVIDIA/nvidia-docker)

For Ubuntu 14.04/16.04/18.04, Debian Jessie/Stretch

```bash
# Add the package repositories
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \
  sudo apt-key add -
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-docker.list
sudo apt-get update

# Install nvidia-docker2 and reload the Docker daemon configuration
sudo apt-get install -y nvidia-docker2
sudo pkill -SIGHUP dockerd

# Test nvidia-smi with the latest official CUDA image
docker run --runtime=nvidia --rm nvidia/cuda:9.0-base nvidia-smi
```

### 2. SKIL client
**python client**: [https://pypi.org/project/skil/](https://pypi.org/project/skil/)

SKIL's Python client can be SKIL's Docker Imagenstalled from PyPI:

```bash
pip install skil --user
```

**java client (TODO)**

## Getting started

## Features

### 1. Textual Information
* NLP
* Text Classification
* Word2Vec

### 2. Image & Video (TODO)
* [Keras MNIST](notebooks/keras-mnist)
* [YOLO2](notebooks/tensorflow-yolo)
* ImageNet
	* InceptionV3
	* Xception
* VGG

### 3. Numerical and Categorical Information

### 4. Time series

## References:
* []()
* []()


