# -*- coding: utf-8 -*-
{
    'name': "Peru - Invoice Documents",

    'summary': """
        Peru - Invoice Documents""",

    'description': """
        Peru - Invoice Documents
    """,

    'author': "GRUPO QUANAM S.A.C.",
    'website': "https://www.grupoquanam.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Quanam Localization',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'l10n_latam_base',
        'l10n_latam_invoice_document',
        'l10n_pe',
    ],

    # always loaded
    'data': [
        'views/views.xml',
    ]
}
