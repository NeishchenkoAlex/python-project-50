install:
	uv sync

build:
	uv build

reinstall:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check --fix

check: test lint

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=hexlet_python_package --cov-report xml