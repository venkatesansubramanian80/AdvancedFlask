from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from users.routes import user_api_bluepring
import models

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

app.config.update(dict(
    SECRET_KEY="thisissecret",
    SQLALCHEMY_DATABASE_URI='sqlite://///app/login.db',
))

models.init_app(app)
models.create_table(app)

app.register_blueprint(user_api_bluepring)


@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
