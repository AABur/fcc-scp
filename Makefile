install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=fcc_scp --cov-report xml

lint:
	poetry run flake8 fcc_scp

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build
