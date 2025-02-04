# Nome da imagem e contêiner
IMAGE_NAME = dev-llvm-environment
CONTAINER_NAME = llvm-dev-container

# Construir a imagem Docker
build:
	docker build -t $(IMAGE_NAME) .

# Executar o contêiner
run:
	docker run -it --rm \
		-v $(PWD):/project \
		--name $(CONTAINER_NAME) \
		$(IMAGE_NAME)

# Parar e remover o contêiner se estiver rodando
stop:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true

# Remover a imagem
clean-image:
	docker rmi $(IMAGE_NAME) || true

# Limpar todos os recursos (contêiner, imagem, volumes não utilizados)
clean-all: stop clean-image
	docker system prune -f
	docker volume prune -f

# Reconstruir a imagem e executar o contêiner
rebuild: clean-all build run

# Listar contêineres e imagens relacionadas
list:
	@echo "Imagens:"
	@docker images | grep $(IMAGE_NAME)
	@echo "\nContêineres:"
	@docker ps -a | grep $(CONTAINER_NAME)

.PHONY: build run stop clean-image clean-all rebuild list
