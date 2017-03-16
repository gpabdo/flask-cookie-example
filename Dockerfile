FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY app /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "gunicorn", "api:app", "--bind", "0.0.0.0:5000","--access-logfile", "/dev/stdout", "--error-logfile", "/dev/stderr"]
