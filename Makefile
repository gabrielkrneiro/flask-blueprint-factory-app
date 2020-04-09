help:
	@echo "check	-	Check required principal dependencies"
	@echo "init		-	Initialize the project"
	@echo "runserver	-	Run the application"
	@echo "test		-	Run unit tests"

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
	@echo "Warning: You should remove migrations/ or data.db if these files already exists"
	poetry run flask db init
	poetry run flask db migrate