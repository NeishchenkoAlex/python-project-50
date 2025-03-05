install:
	uv sync

build:
	uv build

reinstall:
	uv build
	uv tool install --force dist/*.whl