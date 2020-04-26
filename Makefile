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
	[ ! -f ./flask_auth/.env ] && echo "\n# Error: Required file ".env" not exists, create it based on ".env.example" and try it again!\n" && exit 2 || echo ""
	pip install poetry
	poetry install
	@make db-init

db-init:
	@echo "\n#### Removing data.db and migrations if they exists.... ####"
	[ -f ./flask_auth/data.db ] && rm data.db || echo ""
	[ -d "./flask_auth/migrations" ] && rm -rf ./flask_auth/migrations || echo ""
	@echo "\n#### Initializing database.... ####"
	cd flask_auth; poetry run flask db init
	@echo "\n#### Migrating models.... ####"
	cd flask_auth; poetry run flask db migrate
	@echo "\n#### Upgrading database based on current models.... ####"
	cd flask_auth; poetry run flask db upgrade
	@make db-init-test

######################## 	Test scripts	####################################
db-init-test:
	@echo "\n#### Preparing test database environment.... ####"
	[ -f ./data_test.db ] && rm ./data_test.db || echo ""
	APPLICATION_ENV=Test FLASK_APP=flask_auth.run:app poetry run flask db upgrade --directory flask_auth/migrations
	@mv data_test.db ./flask_auth/
	
test:
	@make db-init-test
	@echo "\n#### Running flask_auth.tests.... ####"
	cd flask_auth; poetry run coverage run --source=flask_auth.app -m unittest --verbose flask_auth.test
	@echo "\n#### Running flask_auth.tests.... ####"

html-report:
	cd flask_auth; poetry run coverage html



######################## 	Environment configuration	####################################

runserver:
	cd flask_auth; poetry run python run.py

runserver-prod-dev:
	cd flask_auth; APPLICATION_ENV=Production poetry run gunicorn -c gunicorn.conf.py run:app

runserver-prod:
	cd flask_auth; gunicorn -c gunicorn.conf.py run:app