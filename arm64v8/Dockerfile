
FROM arm64v8/ubuntu:18.04


ENV DEBIAN_FRONTEND=noninteractive


RUN apt-get update && apt-get install -y \
    build-essential \
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
    python3-pip \
    python3-dev \
    openjdk-11-jdk \
    zlib1g-dev



RUN apt-get update && apt-get install -y \
    cmake \
    pkg-config \
    libclang-dev \
    clang \
    llvm \
    openjdk-11-jdk \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


#ENV PATH=/usr/local/bin:$PATH


WORKDIR /project


CMD ["/bin/bash"]

