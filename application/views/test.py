# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/10/15 17:14

from flask import Blueprint, url_for


test_bp = Blueprint('test', __name__, subdomain="<subdomin>")


@test_bp.route('/')
def test_arrival(subdomin):
    return "<h2 style='color:red'>%s</h2>" % url_for("test.test_arrival")


@test_bp.route('/index')
def test_sub_domain():
    return "success"