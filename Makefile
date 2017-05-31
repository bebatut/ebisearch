init:
	python setup.py install

develop:
	python setup.py develop

test:
	flake8 --exclude=.git,build .
	python setup.py test

upload:
	python setup.py register -r pypi
	python setup.py sdist upload -r pypi


.PHONY: init test