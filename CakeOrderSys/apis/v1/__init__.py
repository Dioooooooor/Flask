# -*- coding: utf-8 -*-
'''
    @author: Dioooooooor (曹琛)
    @time: 2019.1.21
    @version: 1.0
    @desc: api端口路由
'''
from flask import Blueprint
from flask_cors import CORS

api_v1 = Blueprint('api_v1', __name__)

CORS(api_v1)

from CakeOrderSys.apis.v1 import resources
