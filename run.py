from flask_auth.app import main_app

if __name__ == "__main__":
    app = main_app()
    app.run(host=app.config['HOST'] or 'localhost',
            port=app.config['PORT'] or '5000')
