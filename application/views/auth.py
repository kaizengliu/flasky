# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/09/28 14:36

from flask import render_template, request, redirect
from flask.blueprints import Blueprint

from application.forms.user import LoginForm
from application.models.user import User

auth_bp = Blueprint('auth', __name__, template_folder="../templates")


@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm(request)

    context = {
        "form": form
    }

    if request.method == 'POST' and form.validate_on_submit():
        # email = form.data.email.strip().lower()
        # password = form.data.email.strip()
        #
        # user = User.query.filter(User.email==email).fisrt()
        # if user.verify_password(password):
        return redirect("index.index")

    return render_template("auth/login.html", **context)