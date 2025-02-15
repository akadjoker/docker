# Use a imagem base do Ubuntu
FROM ubuntu:20.04

# Evita prompts interativos durante a instalação
ENV DEBIAN_FRONTEND=noninteractive

# Instala dependências necessárias
RUN apt-get update && apt-get install -y \
    curl \
    git \
    unzip \
    xz-utils \
    libglu1-mesa \
    openjdk-11-jdk \
    wget \
    cmake \
    ninja-build \
    clang \
    pkg-config \
    libgtk-3-dev \
    && rm -rf /var/lib/apt/lists/*

# Define variáveis de ambiente
ENV ANDROID_SDK_ROOT /opt/android-sdk
ENV FLUTTER_HOME /opt/flutter
ENV PATH $PATH:$FLUTTER_HOME/bin:$ANDROID_SDK_ROOT/cmdline-tools/latest/bin:$ANDROID_SDK_ROOT/platform-tools

# Instala o Android SDK
RUN mkdir -p ${ANDROID_SDK_ROOT} \
    && wget -q https://dl.google.com/android/repository/commandlinetools-linux-8512546_latest.zip -O /tmp/sdk.zip \
    && unzip -q /tmp/sdk.zip -d ${ANDROID_SDK_ROOT} \
    && rm /tmp/sdk.zip \
    && mkdir -p ${ANDROID_SDK_ROOT}/cmdline-tools/latest \
    && mv ${ANDROID_SDK_ROOT}/cmdline-tools/bin ${ANDROID_SDK_ROOT}/cmdline-tools/latest/ \
    && mv ${ANDROID_SDK_ROOT}/cmdline-tools/lib ${ANDROID_SDK_ROOT}/cmdline-tools/latest/

# Aceita licenças do Android SDK
RUN yes | sdkmanager --licenses \
    && sdkmanager "platform-tools" "platforms;android-33" "build-tools;33.0.0"

# Instala o Flutter
RUN git clone https://github.com/flutter/flutter.git $FLUTTER_HOME \
    && cd $FLUTTER_HOME \
    && git checkout stable \
    && flutter precache \
    && flutter doctor

# Define o diretório de trabalho
WORKDIR /app

# Comando padrão
CMD ["bash"]
