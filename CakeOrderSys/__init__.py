# -*- coding: utf-8 -*-
'''
    @author: Dioooooooor
    @time: 2018.12.15
    @version: 1.0
    @desc: 启动文件
'''

import os
import click

from flask import Flask, render_template, request
from CakeOrderSys.extensions import bootstrap, db, login_manager

from CakeOrderSys.blueprints.home import home_bp
from CakeOrderSys.blueprints.login import login_bp
from CakeOrderSys.blueprints.manager import manager_bp
from CakeOrderSys.apis.v1 import api_v1
from CakeOrderSys.models import Admin, Commodity
from CakeOrderSys.settings import config

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    app = Flask('CakeOrderSys')
    app.config.from_object(config[config_name])

    app.config['UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')
    app.config['PRIMARYICON_UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    return app

def register_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(manager_bp)
    app.register_blueprint(api_v1, url_prefix='/api/v1')
    app.register_blueprint(api_v1, subdomain='api', url_prefix='/v1')


def register_commands(app):
    @app.cli.command()
    @click.option('--drop', is_flag=True, help='Create after drop.')
    def initdb(drop):
        """Initialize the database."""
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables.')
        db.create_all()
        click.echo('Initialized database.')
    
    @app.cli.command()
    @click.option('--username', prompt=True)
    @click.password_option()
    def addadmin(username, password):
        """添加管理者账号"""
        admin = Admin.query.filter(Admin.username==username).first()
        if admin is not None:
            click.echo("账号已存在，更新密码")
            admin.set_password(password)
            return
        else:
            click.echo("账号不存在，创建新密码")
            admin = Admin(
                username=username
            )
            admin.set_password(password)
            db.session.add(admin)
        db.session.commit()
        click.echo("InitAdmin Done!")