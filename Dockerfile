FROM python:3.8.6-slim-buster

#create and set working directly
RUN mkdir /serilase
WORKDIR /serilase

#Add the current directory code to working directory
ADD . /serilase/

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# set project environment variables
# grab these via Python's os.environ
# these are 100% optional here
ENV PORT=8000

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        gcc \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install environment dependencies
RUN pip3 install --upgrade pip
RUN pip3 install pipenv
RUN pip3 install -r requirements.txt

#FROM python:3.8.6-slim-buster
#ENV PYTHONUNBUFFERED 1
#
## Install system dependencies
#RUN apt-get update && apt-get install -y --no-install-recommends \
#        tzdata \
#        gcc \
#        python3-setuptools \
#        python3-pip \
#        python3-dev \
#        python3-venv \
#        git \
#        && \
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/*
#
#
#RUN mkdir serilase
#WORKDIR serilase
#COPY ./serilase serilase
#
## install environment dependencies
#RUN pip3 install --upgrade pip
#RUN pip3 install pipenv
#RUN pip3 install -r requirements.txt
#
#
#
#RUN adduser -D user
#USER user
