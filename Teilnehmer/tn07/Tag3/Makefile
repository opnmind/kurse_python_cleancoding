.PHONY: run

SHELL=/bin/bash
VENV=/home/coder/Workspace/kurse_python_cleancoding/.venv
VENV_BIN=$(VENV)/bin/activate
SRC=./src

run:
	source $(VENV_BIN); $(SRC)/app.py

pylint:
	source $(VENV_BIN); pylint $(SRC)

black:
	source $(VENV_BIN); black $(SRC)

mypy: clean-mypy
	mypy $(SRC)

flake:
	source $(VENV_BIN); flake8 $(SRC)

test:
	source $(VENV_BIN); pytest ./tests

clean: clean-pyc clean-build

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	name '*~' -exec rm --force  {}

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

clean-mypy:
	rm --force --recursive .mypy_cache