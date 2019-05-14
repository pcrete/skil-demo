


```bash
#!/usr/bin/env bash

# This contains the SKIL environment variables for the server process.
# See https://docs.skymind.ai for details.

# On first boot these values will be saved to zookeeper.
# Uncomment the line below if you want to overwrite zookeeper values.
FORCE_APPLY_CONF=true

SKIL_HOME=/opt/skil
SKIL_LOG_DIR=/var/log/skil
SKIL_PID_FILE=/var/run/skil/skil.pid

SKIL_CLASS_PATH=/opt/skil/cuda/*:/opt/skil/lib/*:/opt/skil/native/*:/etc/skil/*
SKIL_BACKEND=gpu

SKIL_LICENSE_PATH=/etc/skil/license.txt
SKIL_PUBLIC_KEY_PATH=/etc/skil/publickey.txt

JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
JDK_HOME=$JAVA_HOME

SKIL_SERVER_PROD_MODE=true

ZOOKEEPER_HOST=localhost
ZOOKEEPER_EMBEDDED=true

DEFAULT_ZEPPELIN_BACKEND=gpu
DEFAULT_ZEPPELIN_JVM_ARGS=-Xmx16g -Dorg.bytedeco.javacpp.maxbytes=16G -Dorg.bytedeco.javacpp.maxphysicalbytes=16G -Dorg.nd4j.versioncheck=false -Dorg.deeplearning4j.config.custom.enabled=false

PYTHONPATH="/opt/skil/miniconda/:/opt/sparkHome/python"
PYTHONHTTPSVERIFY=0

# Export variables for use with scripts.
export SKIL_HOME
export SKIL_CLASS_PATH
export SKIL_LOG_DIR
export SKIL_PID_FILE
export SKIL_BACKEND

export SKIL_LICENSE_PATH
export SKIL_PUBLIC_KEY_PATH

export JAVA_HOME
export JDK_HOME

export SKIL_SERVER_PROD_MODE

export ZOOKEEPER_HOST
export ZOOKEEPER_EMBEDDED
export DEFAULT_ZEPPELIN_BACKEND
export DEFAULT_ZEPPELIN_JVM_ARGS

```

export PYTHONPATH
export PYTHONHTTPSVERIFY
