FROM ubuntu:20.04

RUN apt-get update -y; apt-get upgrade -y

RUN apt install python3-pip -y

COPY requirements.txt /webapp/requirements.txt

WORKDIR /webapp

RUN pip3 install -r requirements.txt

COPY . /webapp
