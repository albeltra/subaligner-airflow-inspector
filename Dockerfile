# Subaligner Ubuntu 20 Docker Image
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Los_Angeles

RUN ["/bin/bash", "-c", "apt-get -y update &&\
    apt-get -y install ffmpeg"]

RUN apt-get install -y wget

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O Miniconda3-latest-Linux-x86_64.sh &&\
    chmod +x Miniconda3-latest-Linux-x86_64.sh &&\
    bash Miniconda3-latest-Linux-x86_64.sh -b
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN mkdir /scripts

RUN mkdir -p /airflow/xcom

COPY ./inspect.py /scripts/
ENTRYPOINT ["python3", "/scripts/inspect.py"]
