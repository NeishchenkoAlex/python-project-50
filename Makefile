install:
	uv sync

build:
	uv build

reinstall:
	uv tool install --force dist/*.whl


check: 
	uv run ruff check gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

