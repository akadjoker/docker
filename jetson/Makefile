IMAGE_NAME = jetson-nano-dev
CONTAINER_NAME = jetson-nano-container

# Plataforma alvo
PLATFORM ?= linux/arm64

# Construir a imagem Docker
build:
	docker buildx build \
		--platform $(PLATFORM) \
		-t $(IMAGE_NAME) \
		.

# Executar o contêiner
run:
	docker run -it --rm \
		-v $(PWD):/project \
		--name $(CONTAINER_NAME) \
		$(IMAGE_NAME)

# Verificar versões
verify:
	docker run -it --rm \
		$(IMAGE_NAME) \
		bash -c "\
			python3 --version && \
			pip3 --version"

# Limpar imagem
clean-image:
	docker rmi $(IMAGE_NAME) || true

# Reconstruir
rebuild: clean-image build

.PHONY: build run verify clean-image rebuild
