# Simple Kubernetes Deployment

## Getting started


### 1. Single docker container

```bash
docker run --rm -it -p 3000:80 tutum/hello-world
```

### 2. Kubernetes deployment
```bash
$ kubectl create -f deployment.yaml
```


```yaml
---
kind: Service
apiVersion: v1
metadata:
  name: hello-world-service
spec:
  selector:
    app: hello-world
  ports:
    - protocol: "TCP"
      # Port accessible inside cluster
      port: 8080
      # Port to forward to inside the pod
      targetPort: 80
      # Port accessible outside cluster
      nodePort: 30001
  type: LoadBalancer
 
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-world-deployment
spec:
  replicas: 5
  template:
    metadata:
      labels:
        app: hello-world
    spec:
      containers:
        - name: hello-world
          image: tutum/hello-world
          ports:
            - containerPort: 80

```

## Reference

* [https://github.com/StephenGrider/DockerCasts](https://github.com/StephenGrider/DockerCasts) 
* [https://www.youtube.com/watch?v=1xo-0gCVhTU](https://www.youtube.com/watch?v=1xo-0gCVhTU)