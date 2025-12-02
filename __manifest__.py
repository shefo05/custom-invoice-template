{
    'name': 'STM Modification',
    'version': '18.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Professional Invoice Design Template',
    'author': 'Your Company',
    'depends': ['account', 'sale', 'product', 'stock'],
    'data': [
        'views/report_invoice.xml',
        'views/product_template_views.xml',

    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}