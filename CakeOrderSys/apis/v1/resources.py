# -*- coding: utf-8 -*-
'''
    @author: Dioooooooor (曹琛)
    @time: 2019.1.21
    @version: 1.0
    @desc: 资源视图
'''
from flask import jsonify, request, current_app, url_for, g
from flask.views import MethodView

from CakeOrderSys.apis.v1 import api_v1
from CakeOrderSys.models import Admin, Commodity
from CakeOrderSys.apis.v1.schema import commodity_schema, commodities_schema

class IndexAPI(MethodView):
    def get(self):
        print('get')
        return jsonify({
            "api_version": "1.0",
            "api_base_url": "http://api.caochen.com/v1",
            "current_user_url": "",
            "commodities_url": "http://api.caochen.com/v1/commodities/{?page, per_page}",
            "commodity_url": "http://api.caochen.com/v1/commodities/{commodity_id}",
        })

class CommoditiesAPI(MethodView):
    def get(self):
        "获取所有商品"
        page = request.args.get('page', 1, type=int)
        per_page = 10
        pagination = Commodity.query.paginate(page, per_page)
        commodities = pagination.items
        return jsonify(commodities_schema(commodities, pagination))

api_v1.add_url_rule('/', view_func=IndexAPI.as_view('index'), methods=['GET'])
api_v1.add_url_rule('/commodities', view_func=CommoditiesAPI.as_view('commodities'), methods=['GET','POST'])