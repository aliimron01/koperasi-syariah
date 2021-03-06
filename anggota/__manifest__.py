# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Aggota Koperasi',
    'version': '1.0',
    # 'category': 'Invoicing Management',
    'summary': 'Module anggota koperasi',
    'sequence': '1',
    'author': 'Sidiq Prabowo',
    # 'license': 'LGPL-3',
    'company': 'Bowo',
    'maintainer': 'Sidiq Prabowo',
    'support': 'optimusbow@gmail.com',
    'website': '',
    'depends': ['simpanan'],
    'demo': [],
    'data': [
        'data/ir_sequence_data.xml',
        'views/anggota_views.xml',
        'views/anggota_menu.xml',
        # 'security/ir.model.access.csv',
        # 'security/ir.model.access.csv',
        # 'security/security.xml',
        # 'views/account_pdf_reports.xml',
        # 'wizards/partner_ledger.xml',
        # 'reports/report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
