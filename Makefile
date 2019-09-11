install:
	python -m venv venv

black:
	black . --exclude venv/

lint:
	pylint rskit tests

test:
	pytest tests