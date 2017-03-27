init:
	pip install -r requirements.txt

test:
	flake8 --exclude=.git,build .
	pytest tests

.PHONY: init test