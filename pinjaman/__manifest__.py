# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Pinjaman Anggota Koperasi',
    'version': '1.0',
    # 'category': 'Invoicing Management',
    'summary': 'Module pinjaman anggota koperasi',
    'sequence': '1',
    'author': 'Sidiq Prabowo',
    # 'license': 'LGPL-3',
    'company': 'Bowo',
    'maintainer': 'Sidiq Prabowo',
    'support': 'optimusbow@gmail.com',
    'website': '',
    'depends': [],
    'demo': [],
    'data': [
        'data/ir_sequence_data.xml',
        'views/pinjaman_views.xml',
        'views/pinjaman_menu.xml',
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
