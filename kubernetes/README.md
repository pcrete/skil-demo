# KuberSKIL 
> Skymind Kubernetes Orchestrator

## Installation

1. VirtualBox: [https://www.virtualbox.org/wiki/Linux_Downloads](https://www.virtualbox.org/wiki/Linux_Downloads) 

```bash
wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -
sudo apt-get update
sudo apt-get install virtualbox
```
2. Kubectl: [https://kubernetes.io/docs/tasks/tools/install-kubectl/](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

```bash
sudo apt-get update && sudo apt-get install -y apt-transport-https
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt-get install -y kubectl
```


3. minikube: [https://kubernetes.io/docs/tasks/tools/install-minikube/#linux](https://kubernetes.io/docs/tasks/tools/install-minikube/#linux)

```bash
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
  && chmod +x minikube
sudo cp minikube /usr/local/bin && rm minikube
```

 
## Resources
* Kubernetes Tutorial - an Introduction to the Basics: [https://www.keycdn.com/blog/kubernetes-tutorial](https://www.keycdn.com/blog/kubernetes-tutorial)
