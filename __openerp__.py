# -*- coding: utf-8 -*-
{
    'name': "Bons de réception",

    'summary':	"""
	Réception de barils
				""",

    'description': """
	Bons de réception de barils, enregistrement et suivi des barils dans l'entrepôt.
    """,

    'author': "Global Technologie",
    'website': "http://www.globaltechnologie.ca",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['maplepick'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
		'views/weight_report.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
#        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,

}