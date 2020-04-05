check:
	python --version
	pip --version
	poetry --version

init:
	pip install poetry
	poetry install
	@echo "##### You should create .env file based on .env.example"
	make db-init

runserver:
	poetry run python run.py
	
test:
	poetry run coverage run --source=flask_auth -m unittest --verbose
	poetry run coverage html

db-init:
	flask db init
	flask db migrate
