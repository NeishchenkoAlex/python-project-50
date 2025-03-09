install:
	uv sync

build:
	uv build

reinstall:
	uv build
	uv tool install --force dist/*.whl

lint:
	uv run ruff check --fix

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=hexlet_python_package --cov-report xml