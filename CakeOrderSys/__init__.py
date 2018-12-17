# -*- coding: utf-8 -*-
'''
    :author: Dioooooooor
'''

import os
from flask import Flask, render_template, request

from CakeOrderSys.blueprints.home import home_bp
from CakeOrderSys.blueprints.login import login_bp
from CakeOrderSys.settings import config

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    app = Flask('CakeOrder')
    app.config.from_object(config[config_name])

    register_blueprints(app)

    return app

def register_blueprints(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(login_bp)