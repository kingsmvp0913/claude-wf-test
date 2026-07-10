{
    'name': 'Sale Quotation Stats',
    'version': '17.0.1.0.0',
    'depends': ['sale'],
    'data': [
        'views/sale_order_views.xml',
        'reports/report_quotation_stats.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'idx_sale_stats/static/src/js/quotation_list_controller.js',
            'idx_sale_stats/static/src/js/quotation_stats_dashboard.js',
            'idx_sale_stats/static/src/xml/quotation_list_buttons.xml',
            'idx_sale_stats/static/src/xml/quotation_stats_dashboard.xml',
        ],
        'web.assets_tests': [
            'idx_sale_stats/static/tests/tours/quotation_stats_tour.js',
            'idx_sale_stats/static/tests/tours/quotation_stats_filter_tour.js',
            'idx_sale_stats/static/tests/tours/quotation_stats_state_date_filter_tour.js',
        ],
    },
    'license': 'LGPL-3',
}
