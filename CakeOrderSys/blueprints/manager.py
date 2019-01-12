# -*- coding: utf-8 -*-
'''
    @author: Dioooooooor
    @time: 2018.12.15
    @version: 1.0
    @desc: 商品管理视图
'''
import os
import uuid

from flask import Blueprint, request, render_template, redirect, url_for, current_app, send_from_directory
from flask_login import login_user, logout_user, login_required, current_user
from CakeOrderSys.forms import CommodityForm
from CakeOrderSys.models import Commodity
from CakeOrderSys.extensions import db

manager_bp = Blueprint("manager", __name__)

@manager_bp.route('/manager')
def managerhome():
    if current_user.is_authenticated:
        return render_template('manager/overview.html')
    return redirect(url_for('login.login'))

@manager_bp.route('/create',methods=['GET', 'POST'])
def create():
    form = CommodityForm()
    if form.validate_on_submit():
        f = form.primaryIcon.data
        filename = random_filename(f.filename)
        f.save(os.path.join(current_app.config['PRIMARYICON_UPLOAD_PATH'], filename))
        print(form)
        print(form.name.data,form.price.data,form.detail.data)
        commodity = Commodity(
            name=form.name.data,
            price=form.price.data,
            detail=form.detail.data,
            primaryicon=filename
        )
        db.session.add(commodity)
        db.session.commit()
    return render_template('manager/create.html', form=form)


def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename

@manager_bp.route('/get_primaryicon/<path:filename>')
def get_primaryicon(filename):
    return send_from_directory(current_app.config['PRIMARYICON_UPLOAD_PATH'], filename)

@manager_bp.route('/showallcommoditys')
def showallcommoditys():
    commoditys = Commodity.query.all()
    return render_template('manager/commodity.html', commoditys=commoditys)