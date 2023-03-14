Local Development
Install Pyenv  
pyenv virtualenv 3.11.2 cmg  
pyenv local cmg  
pip install poetry  
poetry init
python process.py log

Containerized
install docker
docker build -t 365widgets .
docker run

Kubernetes
install minikube
kubectl apply -k job/