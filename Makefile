SHELL=/bin/bash
PATH := .venv/bin:$(PATH)
export TEST?=./tests
export ENV?=dev
IMAGE_NAME=creditsim-api


install-local:
	uv sync --all-groups

setup:
	@if [ ! -f .env ] ; then cp .env.mock .env ; fi;
	@make install;

lint: 
	@uv run ruff check .
	@uv run ruff format --check .

lint-fix:
	@uv run ruff check . --fix
	@uv run ruff format .


run-local:
	@docker compose up -d db_dev;
	@uv run uvicorn main:app --reload

build-dev:
	docker build --no-cache -f deploy/dev/Dockerfile -t $(IMAGE_NAME):dev .

run-dev:
	docker run --rm -p 8000:8000 $(IMAGE_NAME):dev

.PHONY: run-local install-local lint lint-fix setup build-dev run-dev