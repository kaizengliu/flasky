# -*-coding: utf-8-*-
# time: 2015/09/16 22:49
# author: liukaizeng

from flask import render_template
from flask.blueprints import Blueprint

index_bp = Blueprint('index', __name__)


@index_bp.route('/')
def index():
    return 'hello world'


@index_bp.route('/add')
def hello_world():
    return '<h1 style="color:red;">hello liuqingqing</h1>'

