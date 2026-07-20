{
    'name': 'Partner Sales Rep',
    'version': '17.0.1.0.0',
    'depends': ['sale'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'assets': {
        'web.assets_tests': [
            'idx_partner_sales_rep/static/tests/tours/partner_sales_rep_tour.js',
            'idx_partner_sales_rep/static/tests/tours/sale_order_sales_rep_tour.js',
        ],
    },
    'license': 'LGPL-3',
}
