init:
	python setup.py install

test:
	flake8 --exclude=.git,build .
	pytest tests

.PHONY: init test