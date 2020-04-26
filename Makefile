######################## 	Help	####################################

help:
	@echo "Commands:"
	@echo "	check		Check required principal dependencies"
	@echo "	init		Initialize the project"
	@echo "	runserver	Run the application"
	@echo "	test		Run unit tests"
	@echo "	db-init		Configure database to development and test environments"
	@echo "	html-report		Generate report as html"
	@echo "	db-init		Configure database to development and test environments"
	@echo "	db-init		Configure database to development and test environments"

check:
	python --version
	pip --version
	poetry --version

######################## 	Environment configuration	####################################
init:
	[ ! -f ./.env ] && echo "\n# Error: Required file ".env" not exists, create it based on ".env.example" and try it again!\n" && exit 2 || echo ""
	pip install poetry
	poetry install
	@make db-init

db-init:
	@echo "\n#### Removing data.db and migrations if they exists.... ####"
	[ -f ./data.db ] && rm data.db || echo ""
	[ -d "./migrations" ] && rm -rf ./migrations || echo ""
	@echo "\n#### Initializing database.... ####"
	poetry run flask db init
	@echo "\n#### Migrating models.... ####"
	poetry run flask db migrate
	@echo "\n#### Upgrading database based on current models.... ####"
	poetry run flask db upgrade
	@make db-init-test

######################## 	Test scripts	####################################
db-init-test:
	@echo "\n#### Preparing test database environment.... ####"
	[ -f ./data_test.db ] && rm ./data_test.db || echo ""
	APPLICATION_ENV=Test FLASK_APP=app.run:app poetry run flask db upgrade --directory app/migrations
	@mv data_test.db ./app/
	
test:
	@make db-init-test
	@echo "\n#### Running app.tests.... ####"
	cd app; poetry run coverage run --source=app.flask_auth -m unittest --verbose app.test
	@echo "\n#### Running app.tests.... ####"

html-report:
	cd app; poetry run coverage html



######################## 	Environment configuration	####################################

runserver:
	cd app; poetry run python run.py

runserver-prod:
	cd app; APPLICATION_ENV=Production gunicorn -c gunicorn.conf.py run:app