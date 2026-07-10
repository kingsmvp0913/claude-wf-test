from odoo.tests import HttpCase, tagged


@tagged('post_install', '-at_install')
class TestSaleQuotationStatsFilter(HttpCase):

    def setUp(self):
        super().setUp()
        self.partner_a = self.env['res.partner'].create({'name': 'StatsTourCustomerA'})
        self.partner_b = self.env['res.partner'].create({'name': 'StatsTourCustomerB'})
        self.product = self.env['product.product'].create({'name': 'Stats Filter 測試商品'})
        self.env['sale.order'].create({
            'partner_id': self.partner_a.id,
            'order_line': [(0, 0, {
                'product_id': self.product.id,
                'product_uom_qty': 1,
            })],
        })
        self.env['sale.order'].create({
            'partner_id': self.partner_b.id,
            'order_line': [(0, 0, {
                'product_id': self.product.id,
                'product_uom_qty': 1,
            })],
        })

    def test_quotation_stats_filter_tour(self):
        self.start_tour('/odoo/sales', 'idx_sale_stats_filter_tour', login='auto_test_user')
