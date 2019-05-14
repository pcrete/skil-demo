## Installation

#### Skymindops/skil-ce
[https://hub.docker.com/r/skymindops/skil-ce](https://hub.docker.com/r/skymindops/skil-ce)


```bash
# pull the SKIL image
docker pull skymindops/skil-ce

# run the SKIL server
docker run --rm -it -p 9008:9008 skymindops/skil-ce bash /start-skil.sh

# Persisting data with Zookeeper
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

# stop SKIL and Zookeeper with:
docker stop skil
docker stop zookeeper

# start it back again with:
docker start zookeeper
docker run --rm -it --name skil -v skil-data:/var/skil --env SKIL_EMBEDDED_DB_PATH=/var/skil/skildb --env ZOOKEEPER_EMBEDDED=false --env ZOOKEEPER_HOST=zookeeper --env ZOOKEEPER_PORT=2181 --link zookeeper:zookeeper -p 9008:9008 -p 8080:8080 skymindops/skil-ce bash /start-skil.sh
```
