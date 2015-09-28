# -*-coding: utf-8-*-
# time: 2015/09/16 22:49
# author: liukaizeng

from flask import render_template
from flask.blueprints import Blueprint
from flask.ext.login import login_required

index_bp = Blueprint('index', __name__, template_folder="../templates")


@index_bp.route('/')
def index():
    context = {
        "title": "Hello World"
    }

    return render_template("index/index.html", **context)

@index_bp.route('/login')
def login():
    context = {

    }

    return render_template()

@index_bp.route('/register')
def register():
    pass

@index_bp.route('/add')
def hello_world():
    return '<h1 style="color:red;">hello liuqingqing</h1>'

