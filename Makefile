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

.PHONY: docker-run
docker-run: docker
		docker run \
			-e DEBUG=True \
			-e PORT=8080 \
			-e SECRET_KEY="secret" \
			-e JWT_ACCESS_TOKEN_EXPIRES=15 \
			-p 8080:8080 \
			${REPOSITORY}/${TARGET}:${DOCKERTAG} 

