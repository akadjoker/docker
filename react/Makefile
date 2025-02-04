
PROJECT_NAME ?= my-react-app
PROJECT_TYPE ?= react
IMAGE_NAME = react-mobile-dev
CONTAINER_NAME = react-mobile-container


build:
	docker build -t $(IMAGE_NAME) .


create-project:
	@echo "Criando projeto $(PROJECT_NAME) do tipo $(PROJECT_TYPE)"
	@case "$(PROJECT_TYPE)" in \
		react) \
			docker run -it --rm \
				-v $(PWD):/project \
				$(IMAGE_NAME) \
				bash -c "npx create-react-app $(PROJECT_NAME)"; \
			;; \
		react-native) \
			docker run -it --rm \
				-v $(PWD):/project \
				$(IMAGE_NAME) \
				bash -c "npx react-native init $(PROJECT_NAME)"; \
			;; \
		expo) \
			docker run -it --rm \
				-v $(PWD):/project \
				$(IMAGE_NAME) \
				bash -c "npx create-expo-app $(PROJECT_NAME)"; \
			;; \
		*) \
			echo "Tipo de projeto inválido. Use: react, react-native ou expo"; \
			exit 1; \
			;; \
	esac


run:
	docker run -it --rm \
		-v $(PWD):/project \
		-p 3000:3000 \
		-p 8081:8081 \
		-p 19000:19000 \
		-p 19001:19001 \
		-p 19002:19002 \
		--name $(CONTAINER_NAME) \
		$(IMAGE_NAME) \
		bash


yarn:
	docker run -it --rm \
		-v $(PWD):/project \
		$(IMAGE_NAME) \
		yarn $(CMD)


npm:
	docker run -it --rm \
		-v $(PWD):/project \
		$(IMAGE_NAME) \
		npm $(CMD)


verify:
	docker run -it --rm \
		$(IMAGE_NAME) \
		bash -c "\
			node --version && \
			npm --version && \
			yarn --version && \
			react-native --version"


stop:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true


clean-image:
	docker rmi $(IMAGE_NAME) || true


clean-all: stop clean-image
	docker system prune -f


rebuild: clean-all build


.PHONY: build create-project run yarn npm verify stop clean-image clean-all rebuild
