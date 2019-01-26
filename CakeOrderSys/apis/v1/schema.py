# -*- coding: utf-8 -*-
'''
    @author: Dioooooooor (曹琛)
    @time: 2019.1.22
    @version: 1.0
    @desc: 资源模式
'''
import os
from flask import send_from_directory, current_app, url_for
from CakeOrderSys.blueprints.manager import get_primaryicon

def commodity_schema(commodity):
    #print(os.getenv('FLASK_CONFIG', 'development'))
    img_url = url_for('manager.get_primaryicon', filename=commodity.primaryicon)
    if os.getenv('FLASK_CONFIG', 'development') == "development":
        img_url = 'http://192.168.30.93/uploadImgs/' + commodity.primaryicon

    return {
        'id': commodity.id,
        'name': commodity.name,
        'price': commodity.price,
        'detail': commodity.detail,
        'primaryicon': img_url
    }

def commodities_schema(commodities, pagination):
    return {
        'items': [commodity_schema(commodity) for commodity in commodities],
        'count': pagination.total
    }