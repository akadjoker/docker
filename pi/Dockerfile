# Usa uma imagem base para ARM64 (Raspberry Pi)
FROM arm64v8/ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive



RUN apt-get update && apt-get install -y \
    curl  build-essential \
    software-properties-common \
    wget \
    curl \
    git \
    libbz2-dev \
    libssl-dev \
    libreadline-dev \
    libsqlite3-dev \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    libgdbm-dev \
    libnss3-dev \
    cmake \
    pkg-config \
    python3 \
    python3-pip




WORKDIR /app


#RUN pip3 install requests

#ENV PATH=/usr/local/bin:$PATH



CMD ["/bin/bash"]

