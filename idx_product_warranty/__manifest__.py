{
    'name': 'Product Warranty',
    'version': '17.0.1.0.0',
    'depends': ['product'],
    'data': [
        'views/product_template_views.xml',
    ],
    'assets': {
        'web.assets_tests': [
            'idx_product_warranty/static/tests/tours/warranty_months_tour.js',
        ],
    },
    'license': 'LGPL-3',
}
