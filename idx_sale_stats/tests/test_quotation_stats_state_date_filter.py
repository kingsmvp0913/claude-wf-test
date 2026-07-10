from odoo.tests import HttpCase, tagged


@tagged('post_install', '-at_install')
class TestSaleQuotationStatsStateDateFilter(HttpCase):

    def setUp(self):
        super().setUp()
        self.partner_confirmed = self.env['res.partner'].create({'name': 'StatsStateCustomerConfirmed'})
        self.partner_old = self.env['res.partner'].create({'name': 'StatsStateCustomerOld'})
        self.product = self.env['product.product'].create({'name': 'Stats State Filter 測試商品'})

        self.order_confirmed = self.env['sale.order'].create({
            'partner_id': self.partner_confirmed.id,
            'order_line': [(0, 0, {
                'product_id': self.product.id,
                'product_uom_qty': 1,
            })],
        })
        self.order_confirmed.action_confirm()

        self.order_old = self.env['sale.order'].create({
            'partner_id': self.partner_old.id,
            'date_order': '2000-01-01',
            'order_line': [(0, 0, {
                'product_id': self.product.id,
                'product_uom_qty': 1,
            })],
        })

    def test_quotation_stats_state_filter_tour(self):
        self.start_tour('/odoo/sales', 'idx_sale_stats_state_filter_tour', login='auto_test_user')

    def test_quotation_stats_date_filter_tour(self):
        self.start_tour('/odoo/sales', 'idx_sale_stats_date_filter_tour', login='auto_test_user')
