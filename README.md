# Django GraphQl CRUD operations


## Local Machine

Pre requisites - Miniconda
https://docs.conda.io/en/latest/miniconda.html

Install the dependencies,

```
conda env create -f environment.yaml -n myenv

```
Run unit tests,
```
python manage.py test company
```

Generate coverage report
```
coverage run --source='.' manage.py test company
coverage report
```

Run the server,
```
python manage.py runserver
```
Go to http://localhost:8000

## Docker

Create a docker image using-

```
docker build  -t docker-django-v0.0 .
```

Run in a docker container-

```
sudo docker run -p 8000:8000 docker-django-v0.0
```

Port 8000 is exposed to the host. Go to http://localhost:8000


