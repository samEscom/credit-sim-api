SHELL=/bin/bash
PATH := .venv/bin:$(PATH)
export TEST?=./tests
export ENV?=dev


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

.PHONY: run-local install-local lint lint-fix setup