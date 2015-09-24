# -*-coding: utf-8-*-
# time: 2015/09/16 22:43
# author: liukaizeng

import os

from flask import Flask, url_for

from application.configure import setting

import views

Blueprints = (
    (views.index_bp, ''),
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
            return

        filename = values.get('filename', None)
        if not filename:
            return

        file_path = os.path.join(app.root_path, endpoint, filename)
        values['q'] = int(os.stat(file_path).st_mtime)

        return url_for(endpoint, **values)


def create_app(configure=None):
    _app = Flask(setting.APP_NAME)

    configure and _app.config.from_object(configure)

    configure_blueprints(_app, Blueprints)
    #configure_url_for_with_timestamp(_app)

    return _app


app = create_app(setting)

if __name__ == '__main__':
    app.run()

