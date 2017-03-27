init:
	pip install -r requirements.txt
	pip install --editable .

test:
	flake8 --exclude=.git,build .
	pytest tests

.PHONY: init test