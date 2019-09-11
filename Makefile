install:
	python -m venv venv

black:
	black . --exclude venv/

lint:
	pylint rkit tests

test:
	pytest tests