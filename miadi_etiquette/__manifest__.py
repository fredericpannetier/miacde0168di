# -*- coding: utf-8 -*-
{
    'name': "MIADI_Etiquette",
    'version' : '1.0',
    'summary': 'Print with EPL/ZPL file on TCP/IP printer',
    'description': """
        Register your TCP/IP printer and your label file in the database and associate both
        in order to print in any situation your label, saved in files which contains
        EPL/ZPL printer command 
    """,

    'author': "MIADI",
    'website': "https://www.groupeadinfo.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Print',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        "views/parameter_views.xml",
        "views/printer_views.xml",
        "views/wiz_print_label.xml",
        "views/label_model_views.xml",
        "miadi_etiquette_menu.xml",
    ],
    
    'installable': True,
    'application': False,
    'auto_install': False,
}