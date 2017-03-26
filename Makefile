init:
	pip install -r requirements.txt

test:
	flake8 --exclude=.git,build .
	py.test tests

.PHONY: init test