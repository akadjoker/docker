# Variáveis
IMAGE_NAME = pi
CONTAINER_NAME = pi-container
PLATFORM = linux/arm64


all: build run

# Construir a imagem Docker
build:
	docker buildx build --platform $(PLATFORM) -t $(IMAGE_NAME) --load .

# Executar o contêiner
run:
	docker run --rm --platform $(PLATFORM) --name $(CONTAINER_NAME) $(IMAGE_NAME)


   


# Limpar contêineres e imagens
clean:
	docker rm -f $(CONTAINER_NAME) || true
	docker rmi $(IMAGE_NAME) || true

# Executar um shell interativo no contêiner
#shell:
	#docker run  --rm -it --platform linux/arm64 -v $(pwd):/app --name $(CONTAINER_NAME) $(IMAGE_NAME)  /bin/bash

shell:
	docker run --rm -it --platform linux/arm64 -v $(shell pwd):/app --name pi-container pi /bin/bash







help:
	@echo "Comandos disponíveis:"
	@echo "  make build    - Construir a imagem Docker"
	@echo "  make run      - Executar o contêiner"
	@echo "  make clean    - Remover contêineres e imagens"
	@echo "  make shell    - Executar um shell interativo no contêiner"
	@echo "  make help     - Exibir esta mensagem de ajuda"
