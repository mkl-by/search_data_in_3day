FROM ubuntu:latest
RUN apt update
RUN apt -y upgrade
RUN apt -y install python3-pip
RUN mkdir /src
WORKDIR /src
COPY ./requirements.txt /scripts/
RUN pip install -r /scripts/requirements.txt