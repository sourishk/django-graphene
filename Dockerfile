FROM continuumio/miniconda3

ENV DOCKER_HOME=/home/main
RUN mkdir -p $DOCKER_HOME
WORKDIR $DOCKER_HOME

COPY environment.yaml .

RUN conda env create -f environment.yaml -n myenv

COPY ./ ./

SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

EXPOSE 8000  

ENTRYPOINT ["conda", "run", "-n", "myenv", "python", "manage.py", "runserver", "0.0.0.0:8000"]
