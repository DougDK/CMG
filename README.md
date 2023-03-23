# Local Development  


Follow the steps below in order to prepare your environment for local development:  

1. Install and configure [Pyenv](https://github.com/pyenv/pyenv)  
1. Run the commands
```bash
cd 365widgets
pyenv virtualenv 3.11.2 cmg
pyenv local cmg
pip install poetry
poetry install
python app/process.py logs/example.log
```

Instead of a parameter you can also use LOG_PATH to define the location of your log file

```bash
export LOG_PATH=~/local/path/to/some.log
python app/process.py
```


# Containerized  


Follow the steps below in order to Build and Run the container solution:  

1. Install docker  
1. Run the commands  
```bash
docker build -t 365widgets .
docker run \
    --name=365widgets \
    365widgets python app/process.py logs/example.log
docker rm -f 365widgets
```

In order to process a different log, you can also use Docker volumes. The LOG_PATH environment variable still valid if necessary.  

```bash
docker volume create 365widgets
docker run -d \
    --name 365widgets \
    --mount source=365widgets,target=/app/365widgets/logs \
    365widgets sleep infinity
docker cp ~/local/path/to/some.log 365widgets:/app/365widgets/logs
docker rm -f 365widgets
docker run \
    --name 365widgets \
    --mount source=365widgets,target=/app/365widgets/logs \
    365widgets python app/process.py logs/some.log
docker rm -f 365widgets
```

The LOG_PATH environment variable still valid in the containerized context.  

```bash
docker run \
    --name=365widgets \
    --mount source=365widgets,target=/app/365widgets/logs \
    -e LOG_PATH=/app/365widgets/logs/some.log \
    365widgets python app/process.py
docker rm -f 365widgets
docker volume rm 365widgets
```


# Kubernetes  


Follow the steps below in order to deploy it into a minikube local cluster:  


1. Install minikube  
1. `minikube start`  
1. `eval $(minikube docker-env)`  
1. `docker build -t 365widgets .`  
1. `kubectl apply -k k8s/`  
1. `kubectl logs job/365widgets -n 365widgets`  
1. `kubectl remove -k k8s/`  
