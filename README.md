# Django GraphQl CRUD operations

Create a docker image using-

```
docker build  -t docker-django-v0.0 .
```

Run in a docker container-

```
sudo docker run -p 8000:8000 docker-django-v0.0
```

Port 8000 is exposed to the host. Go to http://localhost:8000


To run on the local machine, install the dependencies and then start the server.

```
conda env create -f environment.yaml -n myenv
python manage.py runserver
```

Deployment on Kubernetes

For local docker image-
```
kubectl create deployment --image=docker-django-v0.0 docker-django-v0.0-app
```

For docker image hosted on dockerhub, using deployment.yaml

https://docs.docker.com/get-started/kube-deploy/

```
kubectl create -f deployment.yml
```
