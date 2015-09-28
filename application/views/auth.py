# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/09/28 14:36

from flask import render_template, request
from flask.blueprints import Blueprint

from application.forms.user import LoginForm
from application.models.user import User

auth_bp = Blueprint('auth', __name__, template_folder="../templates")


@auth_bp.route('/login')
def login():
    context = {
        "form": LoginForm
    }

    if request.method == 'GET':
        return render_template("auth/login.html", **context)

    if request.method == 'POST':
        form = LoginForm(request)

        if form.validate_on_submit():
            email = form.data.email.strip().lower()
            password = form.data.email.strip()

            user = User.query.filter(User.email==email).fisrt()
            if user.verify_password(password):
                pass
        else:
            context.update(form=LoginForm)
            return render_template("auth/login.html", **context)