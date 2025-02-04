# Use Debian como imagem base
FROM debian:bullseye-slim

# Definir variáveis de ambiente para evitar interações durante a instalação
ENV DEBIAN_FRONTEND=noninteractive

# Atualizar pacotes e instalar dependências essenciais
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    wget \
    git \
    libtool \
    automake \
    pkg-config \
    gnupg \
    software-properties-common \
    ca-certificates

# Adicionar repositório LLVM
RUN wget https://apt.llvm.org/llvm.sh \
    && chmod +x llvm.sh \
    && ./llvm.sh 16 \
    && rm llvm.sh

# Instalar ferramentas do LLVM
RUN apt-get update && apt-get install -y \
    llvm-16 \
    clang-16 \
    lld-16 \
    libc++-16-dev \
    libc++abi-16-dev

# Configurar alternativas para usar LLVM 16
RUN update-alternatives --install /usr/bin/cc cc /usr/bin/clang-16 100 \
    && update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++-16 100 \
    && update-alternatives --install /usr/bin/ld ld /usr/bin/lld-16 100

# Definir diretório de trabalho
WORKDIR /project

# Copiar código fonte (se necessário)
# COPY . /project

# Comando padrão
CMD ["/bin/bash"]
