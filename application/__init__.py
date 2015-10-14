# -*-coding: utf-8-*-
# time: 2015/09/16 22:43
# author: liukaizeng

import os

import redis

from flask import Flask, url_for, sessions
from flask.ext.login import LoginManager, AnonymousUserMixin
from flask.ext.session import RedisSessionInterface

from application.configure import setting
from application.models.user import User

import views

Blueprints = (
    (views.index_bp, ''),
    (views.auth_bp, '/auth')
)


def configure_blueprints(app, blueprints):
    for view, url_prefix in blueprints:
        app.register_blueprint(view, url_prefix=url_prefix)


def configure_url_for_with_timestamp(app):
    @app.context_processor
    def override_url_for():
        return dict(url_for=dated_url_for)

    def dated_url_for(endpoint, **values):
        if endpoint != 'static':
            return url_for(endpoint, **values)

        filename = values.get('filename', None)
        if not filename:
            return url_for(endpoint, **values)

        file_path = os.path.join(app.root_path, endpoint, filename)
        values['q'] = int(os.stat(file_path).st_mtime)

        return url_for(endpoint, **values)


def configure_login_manager(app):
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"

    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(user_id):
        if user_id:
            return User.query.get(user_id)
        else:
            return AnonymousUserMixin()


def configure_redis_session_interface(app):
    redis_client = redis.Redis(setting.REDIS_HOST, setting.REDIS_PORT)
    app.session_interface = RedisSessionInterface(redis_client, 'session:')


def create_app(configure=None):
    _app = Flask(setting.APP_NAME)

    configure and _app.config.from_object(configure)

    configure_blueprints(_app, Blueprints)
    configure_url_for_with_timestamp(_app)
    configure_login_manager(_app)
    configure_redis_session_interface(_app)

    return _app


app = create_app(setting)

if __name__ == '__main__':
    app.run()

