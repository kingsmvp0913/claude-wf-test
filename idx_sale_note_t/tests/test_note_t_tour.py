from odoo.tests import HttpCase, tagged


@tagged('post_install', '-at_install')
class TestSaleNoteT(HttpCase):

    def setUp(self):
        super().setUp()
        self.partner = self.env['res.partner'].create({
            'name': 'Note T 測試客戶',
        })

    def test_note_t_tour(self):
        self.start_tour('/odoo/sales', 'idx_sale_note_t_tour', login='auto_test_user')

    def test_note_t_shown_in_report(self):
        order = self.env['sale.order'].create({
            'partner_id': self.partner.id,
            'note_t': '備註T報表測試內容',
        })
        html, _ = self.env['ir.actions.report']._render_qweb_html(
            'sale.action_report_saleorder', order.ids
        )
        html = html.decode()
        self.assertIn('備註T', html)
        self.assertIn('備註T報表測試內容', html)
