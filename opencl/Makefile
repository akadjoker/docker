# Nome da imagem e do container
DOCKER_IMAGE = dopencl-env
DOCKER_CONTAINER = dev-clang-container

# Diretório de trabalho no container
WORKDIR = /workspace

# Caminho do projeto local
PROJECT_DIR = $(shell pwd)

# Regras principais
.PHONY: build run shell stop clean

# Cria a imagem Docker
build:
	docker build -t $(DOCKER_IMAGE) .

# Inicia o container em modo interativo
run:
	docker run --rm -it -v $(PROJECT_DIR):$(WORKDIR) -w $(WORKDIR) --name $(DOCKER_CONTAINER) $(DOCKER_IMAGE)

# Abre um shell interativo no container (caso já esteja a correr)
shell:
	docker exec -it $(DOCKER_CONTAINER) /bin/bash || docker run --rm -it -v $(PROJECT_DIR):$(WORKDIR) -w $(WORKDIR) --name $(DOCKER_CONTAINER) $(DOCKER_IMAGE)

# Para o container em execução
stop:
	docker stop $(DOCKER_CONTAINER)

# Remove a imagem Docker
clean:
	docker rmi $(DOCKER_IMAGE)

