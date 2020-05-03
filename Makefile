######################## 	Help	####################################

help:
	@echo "Commands:"
	@echo "	check				Check required principal dependencies"
	@echo "	init				Initialize the project"
	@echo "	db-init				Configure database to development and test environments"
	@echo "	db-init-test			Configure database only to test environment"
	@echo "	test				Run unit tests"
	@echo "	html-report			Generate report as html"
	@echo "	lint				Check code linting"
	@echo "	runserver			Run the application in Development mode"
	@echo "	runserver-prod			Run the application in Production mode"
	@echo "	runserver-prod-dev		Run the application in Development but emulating the Production environment"
	@echo "	build				Build the project Docker image"
	@echo "	deploy				Build the projet Docker image and deploy it in Docker Swarm"
	@echo "	run-as-container		Run the application as container"
	@echo "	run-as-temporary-container	Run the application as temporary container, which will be automatically removed if stopped."
	@echo "	clean				Remove not in use Docker objects"
	@echo "	logs				Show service logs"


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
	@echo "\n*** Removing data.db and migrations if they exists...."
	[ -f ./flask_auth/data.db ] && rm data.db || echo ""
	[ -d "./flask_auth/migrations" ] && rm -rf ./flask_auth/migrations || echo ""
	@echo "\n*** Initializing database...."
	cd flask_auth; poetry run flask db init
	@echo "\n*** Migrating models...."
	cd flask_auth; poetry run flask db migrate
	@echo "\n*** Upgrading database based on current models...."
	cd flask_auth; poetry run flask db upgrade
	@make db-init-test

db-init-test:
	@echo "\n*** Preparing test database environment...."
	[ -f ./data_test.db ] && rm ./data_test.db || echo ""
	APPLICATION_ENV=Test FLASK_APP=flask_auth.run:app poetry run flask db upgrade --directory flask_auth/migrations
	@mv data_test.db ./flask_auth/

######################## 	Test scripts	####################################

test:
	@make db-init-test
	@make lint
	@echo "\n*** unit tests...."
	cd flask_auth; poetry run coverage run --source=flask_auth.app -m unittest --verbose flask_auth.test

html-report:
	@echo "\n*** Generating report as htmlconv directory"
	cd flask_auth; poetry run coverage html

lint:
	@echo "\n*** Running linter to check code patterns"
	poetry run flake8 --config=.flake8 flask_auth


######################## 	Environment Servers	####################################

runserver:
	cd flask_auth; poetry run python run.py

runserver-prod-dev:
	APPLICATION_ENV=Production poetry run gunicorn -c flask_auth/gunicorn.conf.py flask_auth.run:app

runserver-prod:
	gunicorn -c flask_auth/gunicorn.conf.py flask_auth.run:app

######################## 	Deployment process	####################################

build:
	@echo "\n*** Building the project...."
	poetry export -f requirements.txt -o requirements.txt
	docker-compose build

deploy:
	@echo "\n*** Running deploy process"
	@make test
	@make build
	docker stack rm flask_auth
	sleep 20
	docker stack deploy -c docker-compose-prod.yml flask_auth

run-as-container:
	@echo "\n*** Run a container based on flask_auth_gabrielcarneirodeveloper:1 image"
	docker run -p 8080:5010 --name flask_auth flask_auth_gabrielcarneirodeveloper:1

run-as-temporary-container:
	@echo "\n*** Run a container based on flask_auth_gabrielcarneirodeveloper:1 image and activate its command line."
	@echo "***Once its a temporary container, it will be automatically removed if stopped."
	docker run --rm -it -p 8080:5010 flask_auth_gabrielcarneirodeveloper:1 /bin/sh

clean:
	@echo "\n !!!!! CAUTION !!!!!!"
	@echo "*** This command will remove all the images, volumes, containers, networks which are not in use currently"
	docker system prune --volumes

logs:
	@echo "\n*** Show flask_auth_web_service logs"
	docker service logs flask_auth_web_service
