from odoo.tests import HttpCase, tagged


@tagged('post_install', '-at_install')
class TestSaleFakeQuotations(HttpCase):

    def test_generate_fake_quotations_tour(self):
        Order = self.env['sale.order']
        before_count = Order.search_count([('note_t', 'like', '自動產生測試備註%')])
        self.start_tour('/odoo/sales', 'idx_sale_note_t_fake_data_tour', login='auto_test_user')
        after_count = Order.search_count([('note_t', 'like', '自動產生測試備註%')])
        self.assertEqual(after_count - before_count, 100)
