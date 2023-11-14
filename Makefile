install:
	poetry install

package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall

build:
	poetry build
