SHELL := /bin/sh

TARGET := dstt

REPOSITORY ?= reidaa
DOCKERFILE ?= Dockerfile
DOCKERTAG ?= latest


.PHONY: format
format:
	black app.py src/
	isort app.py src/

.PHONY: run
run:
	uv run app.py

.PHONY: docker
docker:
		docker build --no-cache -t ${REPOSITORY}/${TARGET}:${DOCKERTAG} -f ${DOCKERFILE} .

.PHONY: up
up:
	docker compose build
	docker compose up -d

.PHONY: down
down:
	docker compose down --remove-orphans
	docker compose rm
