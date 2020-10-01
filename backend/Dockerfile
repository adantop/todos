FROM alpine

LABEL maintainer="https://github.com/adantop"
# remove all finished containers
# docker container rm $(docker container ls -aq)

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

RUN apk add --no-cache python3 py3-pip

RUN mkdir /backend

COPY requirements.txt /backend/requirements.txt
COPY app.py /backend/app.py
COPY todo.py /backend/todo.py

RUN pip install -r /backend/requirements.txt

WORKDIR /backend

EXPOSE 5000

ENTRYPOINT [ "python3", "app.py" ]
