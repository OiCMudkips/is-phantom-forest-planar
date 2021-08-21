.PHONY: install

install:
	pip install -rrequirements-dev.txt
	cd planarity && pip install .

virtualenv_run:
	python3 -m venv virtualenv_run
