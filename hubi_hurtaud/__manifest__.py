# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'hubi_hurtaud',
    'version' : '1.0',
    'summary': 'hubi Hurtaud',
    'author': 'Miadi',
    'description': """
Gestion HUBI - Spécifiques Hurtaud
""",
    
    'depends' : ['base','hubi'],

    'data': ["reports/inherited_sale_order_hubi_report.xml",
             "reports/inherited_account_invoice_hubi_report.xml",
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
