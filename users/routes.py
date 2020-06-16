from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import models

user_api_bluepring = Blueprint('user_api', __name__)


@user_api_bluepring.route('/add_user/<user_name>')
def add_user(user_name):
    new_user = models.User(username=user_name)
    models.db.session.add(new_user)
    models.db.session.commit()
    return "Success"


@user_api_bluepring.route('/get_user/<user_name>')
def get_user(user_name):
    user = models.User.query.filter_by(username=user_name).first()
    login_user(user)
    print(user)
    return "You are now logged in"


@user_api_bluepring.route('/logout')
@login_required
def logout():
    logout_user()
    return "User logged out"


@user_api_bluepring.route('/home')
@login_required
def home():
    return 'the current user is ' + current_user.username