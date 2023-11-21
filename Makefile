install:
	poetry install

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

build:
	poetry build

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
