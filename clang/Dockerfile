FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    make \
    cmake \
    git \
    wget \
    lsb-release \
    software-properties-common \
    gnupg \
    build-essential \
    python3-dev \ 
    libpython3-dev \
    libglfw3-dev \
    libglew-dev \
    libglm-dev \
    libsdl2-dev \
    libx11-dev \
    libxrandr-dev \
    libxi-dev \
    libxxf86vm-dev \
    libxcursor-dev \
    libgl1-mesa-dev \
    libglu1-mesa-dev \
    && apt clean 
    #&& rm -rf /var/lib/apt/lists/*


WORKDIR /workspace

# Comando padrão ao entrar no container
CMD ["/bin/bash"]

