# SKIL: Skymind's Intelligence Layer

This project is introduced in an attempt to demonstrate the use of original repo here: https://github.com/SkymindIO/skil-python
## Installation


### 1. SKIL's docker image
To install SKIL itself, head over to [skymind.ai](https://docs.skymind.ai/docs/docker-image). 

#### Run the SKIL server
```bash
# Pull the SKIL image from the repo
docker pull skymindops/skil-ce
# run the SKIL server
docker run --rm -it -p 9008:9008 skymindops/skil-ce bash /start-skil.sh
```

#### Persisting Data with Zookeeper

To persist your notebooks and model server configurations is to use a separate zookeeper container and use persistent data volumes for zookeeper and SKIL. 

```bash
docker volume create --name zk-data
docker volume create --name zk-datalog
docker volume create --name skil-data
docker pull zookeeper
docker run --name zookeeper -v zk-data:/data -v zk-datalog:/datalog -d zookeeper
docker run --rm -it --name skil -v skil-data:/var/skil \
--env SKIL_EMBEDDED_DB_PATH=/var/skil/skildb \
--env ZOOKEEPER_EMBEDDED=false \
--env ZOOKEEPER_HOST=zookeeper \
--env ZOOKEEPER_PORT=2181 \
--link zookeeper:zookeeper \
-p 9008:9008 -p 8080:8080 skymindops/skil-ce bash /start-skil.sh
```

Now, you can access the SKIL UI by opening a browser window to [http://localhost:9008](http://localhost:9008) 


```bash
# Afterwards you can stop SKIL and zookeeper with:
docker stop skil
docker stop zookeeper
```

### 2. Python client
SKIL's Python client can be SKIL's Docker Imagenstalled from PyPI:

```bash
pip install skil --user
```

## Getting started

## Features

### 1. Natural Language Processing

### 2. Image Recognition


### 3. Object Detection
* Human Detection
* Face Detection

### 4. Anomaly Detection
* Fraud Detection

### 5. Recommendation System




