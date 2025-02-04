
IMAGE_NAME = arm64-dev-env
CONTAINER_NAME = arm64-dev-container


build:
	docker buildx build \
		--platform linux/arm64 \
		-t $(IMAGE_NAME) . --load



create-builder:
	docker buildx create --name multiarch-builder --driver docker-container --use
	docker buildx inspect --bootstrap


run:
	docker run -it --rm \
		-v $(PWD):/project \
		--name $(CONTAINER_NAME) \
		$(IMAGE_NAME)


exec:
	docker run -it --rm \
		-v $(PWD):/project \
		--name $(CONTAINER_NAME) \
		$(IMAGE_NAME) \
		/bin/bash -c "$(CMD)"


verify:
	docker run -it --rm \
		-v $(PWD):/project \
		--name $(CONTAINER_NAME) \
		$(IMAGE_NAME) \
		bash -c "\
			python3 --version && \
			gcc --version && \
			g++ --version && \
			cmake --version"


stop:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true


clean-image:
	docker rmi $(IMAGE_NAME) || true

# Limpar todos os recursos
clean-all: stop clean-image
	docker system prune -f

# Reconstruir a imagem
rebuild: clean-all build

.PHONY: build create-builder run exec verify stop clean-image clean-all rebuild
