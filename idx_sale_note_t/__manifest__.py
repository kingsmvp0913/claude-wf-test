{
    'name': 'Sale Order Note T',
    'version': '17.0.1.0.0',
    'depends': ['sale'],
    'data': [
        'views/sale_order_views.xml',
        'reports/report_saleorder.xml',
    ],
    'assets': {
        'web.assets_tests': [
            'idx_sale_note_t/static/tests/tours/note_t_tour.js',
        ],
    },
    'license': 'LGPL-3',
}
