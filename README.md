# Factory App + Blueprints [Study purpose]

There are many ways to develop a [Flask](https://flask.palletsprojects.com/en/1.1.x/) project and structure its directories. A very known and advised way to do it is using [Factory App](https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/) with [Blueprints](https://flask.palletsprojects.com/en/1.1.x/tutorial/views/). At use these two patterns, is possible to have an easier to debug, readable and well modularized Flask project. This project aims demonstrate how is possible use them.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development, testing and studying purposes. See deployment for notes on how to deploy the project on a live system using Docker.

### Prerequites

To use all project features, it should be in an Unix distro, preference Ubuntu (Sorry about this, but I will try solve it further ;D) and the dependecies bellow.

```
build-essential (to use **make** commands)
Python 3.x
Pip
Docker
docker-compose
```

### Clone the repository

``` shell
git clone https://github.com/GabrielCarneiroDeveloper/flask-blueprint-factory-app.git
```

### Install project dependencies

``` shell
make init
```

### Create .env inside flask_auth directory

Inside **flask-blueprint-factory-app/flask_auth/** directory:

* create **.env** file based on .env.example.
* .env should has two variables: **APPLICATION_ENV** and **FLASK_APP**.
* Configure **APPLICATION_ENV** with one of the possible values: <ins>Development</ins>, <ins>Production</ins> and <ins>Test</ins> (*Exactly as described before, with first letter in upper case*)

### Running server

Run with Flask default server

``` shell
make runserver
```

## Documentation

With the project running, access the documentation in http://localhost:5000/apidocs. The API documentation was created based on [Swagger](https://swagger.io/) using [Flasgger](https://github.com/flasgger/flasgger)

![API Documentation](https://github.com/GabrielCarneiroDeveloper/flask-blueprint-factory-app/blob/master/static/API_documentation.png)

## Commands

To see available commands, run:  

``` shell
make help
```

``` shell
Commands:
        check                           Check required principal dependencies
        init                            Initialize the project
        db-init                         Configure database to development and test environments
        db-init-test                    Configure database only to test environment
        test                            Run unit tests
        html-report                     Generate report as html
        lint                            Check code linting
        runserver                       Run the application in Development mode
        runserver-prod                  Run the application in Production mode
        runserver-prod-dev              Run the application in Development but emulating the Production environment
        build                           Build the project Docker image
        deploy                          Build the projet Docker image and deploy it in Docker Swarm
        run-as-container                Run the application as container
        run-as-temporary-container      Run the application as temporary container, which will be automatically removed if stopped.
        clean                           Remove not in use Docker objects
        logs                            Show service logs
```
## Running Tests

### Unit test

The API unit tests were developed using **unittest** built-in Python module. Run unit tests with the command:

``` shell
make test
```

### Code style

To check code style, was used [Flake8](https://pypi.org/project/flake8/) and formatted using [Black](https://pypi.org/project/black/). Run style checker with the command:

``` shell
make lint
```

## Deployment

If you want run the application server in Docker orchestraded by Swarm:

1) Make your host as a Swarm master, if it isn't yet:

``` shell
docker swarm init
```

2) Run unit tests, linter, and deploy process:

``` shell
make deploy
```

3) Check if stack project's services are running:

``` shell
docker stack services flask_auth
```

``` shell
ID                  NAME                     MODE                REPLICAS            IMAGE                                   PORTS
mitl3o76an26        flask_auth_web_service   replicated          2/2                 flask_auth_gabrielcarneirodeveloper:1   *:8080->5010/tcp

```

## Built with

* **[Flask](https://flask.palletsprojects.com/en/1.1.x/)** - Mainly framework used to develop the project
* **[Flake8](https://pypi.org/project/flake8/)** - Code Linter
* **[Black](https://pypi.org/project/black/)** - Code formatter
* **[Flasgger](https://github.com/flasgger/flasgger)** - Used to build API documentation. It is based on **[Swagger](https://swagger.io/)**
* **[Poetry](https://python-poetry.org/)** - Python package manager

To see all packages, please take a look in **pyproject.toml**

## Authors

* **Gabriel Carneiro** - *Principal developer* - https://github.com/GabrielCarneiroDeveloper

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/GabrielCarneiroDeveloper/flask-blueprint-factory-app/blob/improve-readme/LICENSE) file for details

## Contributing

Please read [CONTRIBUTING.md](https://github.com/GabrielCarneiroDeveloper/flask-blueprint-factory-app/blob/improve-readme/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Contacts

If you have some question, improvement or issues at try to install/run the project, please contact me in my e-mail and i'll be glad to help you: **carneiro.development@gmail.com**. 

### If you like it, please give a star ;D
