# -*- coding: utf-8 -*-
'''
    @author: Dioooooooor
    @time: 2018.12.17
    @version: 1.0
    @desc: 主页视图
'''

from flask import Blueprint, request, render_template
from CakeOrderSys.models import Commodity

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    commoditys = Commodity.query.all()
    return render_template('home/home.html',  commoditys=commoditys)