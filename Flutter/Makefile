
IMAGE_NAME = flutter-docker
CONTAINER_NAME = flutter-container


PROJECT_NAME ?= my_app


build:
	docker  build -t $(IMAGE_NAME) .


create-project:
	docker run --rm -v $(PWD):/app  --user $(shell id -u):$(shell id -g) -w /app $(IMAGE_NAME) flutter create $(PROJECT_NAME)
 

run:
	docker run --rm -v $(PWD):/app -w /app --net=host $(IMAGE_NAME) flutter run


run-web:
	docker run --rm -v $(PWD):/app -w /app --net=host $(IMAGE_NAME) flutter run -d chrome


doctor:
	docker run --rm -v $(PWD):/app -w /app $(IMAGE_NAME) flutter doctor


shell:
	docker run -it --rm -v $(PWD):/app -w /app $(IMAGE_NAME) bash


clean:
	docker rmi $(IMAGE_NAME) || true

