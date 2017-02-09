# -*- coding: utf-8 -*-
from openerp import http

# class Maplereception(http.Controller):
#     @http.route('/maplereception/maplereception/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/maplereception/maplereception/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('maplereception.listing', {
#             'root': '/maplereception/maplereception',
#             'objects': http.request.env['maplereception.maplereception'].search([]),
#         })

#     @http.route('/maplereception/maplereception/objects/<model("maplereception.maplereception"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('maplereception.object', {
#             'object': obj
#         })