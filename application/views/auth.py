# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/09/28 14:36

from flask import render_template, request, redirect, url_for, abort
from flask.blueprints import Blueprint
from flask.ext.login import login_required, login_user, logout_user, current_user
from application.utils.redis_cli import redis_cli

from application.forms.user import LoginForm, RegisterForm
from application.models.base import db_session
from application.models.user import User

auth_bp = Blueprint('auth', __name__, template_folder="../templates")


@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    context = {
        "form": form
    }

    if request.method == 'POST' and form.validate_on_submit():
        return redirect(url_for("index.index"))

    return render_template("auth/login.html", **context)


@auth_bp.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()

    context = {
        'form': form
    }

    if request.method == 'POST' and form.validate_on_submit():
        user = User()
        user.email = form.email.data.strip().lower()
        user.password = form.password.data.strip()
        user.username = user.email

        db_session.add(user)
        db_session.commit()

        login_user(user)

        user.send_register_mail(request.host_url)

        return redirect(url_for("index.index"))

    return render_template("auth/register.html", **context)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("index.index"))


@auth_bp.route('/active_account', methods=['GET'])
def active_account():
    key = request.args.get('key')
    email = request.args.get('email')

    if not key or not email:
        abort(404)

    email = email.strip().lower()

    user_id = redis_cli.get(key)
    user = User.query.get(user_id)

    if user.email == email:
        user.active = True
        db_session.commit()
        login_user(user)

    return redirect(url_for('index.index'))
