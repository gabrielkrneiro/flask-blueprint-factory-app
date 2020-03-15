from flask_auth.app import app

if __name__ == "__main__":
    app.run(port=app.config['PORT'] or '5526')