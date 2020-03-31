default: runserver

runserver:
	poetry run python run.py

test:
	poetry run coverage run --source=flask_auth -m unittest --verbose
	poetry run coverage html
