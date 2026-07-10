from odoo.tests import HttpCase, tagged


@tagged('post_install', '-at_install')
class TestSaleQuotationStats(HttpCase):

    def setUp(self):
        super().setUp()
        self.partner = self.env['res.partner'].create({'name': 'Stats 測試客戶'})
        self.product = self.env['product.product'].create({'name': 'Stats 測試商品'})
        self.order = self.env['sale.order'].create({
            'partner_id': self.partner.id,
            'order_line': [(0, 0, {
                'product_id': self.product.id,
                'product_uom_qty': 2,
            })],
        })

    def test_get_quotation_stats(self):
        stats = self.env['sale.order'].get_quotation_stats([('id', '=', self.order.id)])
        self.assertEqual(len(stats), 1)
        self.assertEqual(stats[0]['partner_id'], self.partner.id)
        self.assertEqual(stats[0]['order_count'], 1)
        self.assertEqual(stats[0]['item_count'], 1)
        self.assertAlmostEqual(stats[0]['percentage'], 100.0)

    def test_quotation_stats_tour(self):
        self.start_tour('/odoo/sales', 'idx_sale_stats_tour', login='auto_test_user')
