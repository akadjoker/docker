
FROM arm64v8/ubuntu:18.04


ENV DEBIAN_FRONTEND=noninteractive


RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    wget \
    curl \
    python3 \
    python3-pip \
    python3-dev \
    software-properties-common 


RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1







ENV PYTHONPATH=/usr/local/lib/python3/dist-packages


WORKDIR /project


CMD ["/bin/bash"]
