# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
'''
    @author: Dioooooooor
    @time: 2018.12.15
    @version: 1.0
    @desc: 启动文件
'''

import os
from flask import Flask, render_template, request
from CakeOrderSys.extensions import bootstrap

from CakeOrderSys.blueprints.home import home_bp
from CakeOrderSys.blueprints.login import login_bp
from CakeOrderSys.settings import config

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    app = Flask('CakeOrderSys')
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)

    return app

def register_extensions(app):
    bootstrap.init_app(app)


def register_blueprints(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(login_bp)