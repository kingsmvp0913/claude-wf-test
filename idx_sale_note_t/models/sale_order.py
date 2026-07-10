import random
from datetime import timedelta

from odoo import fields, models

FAKE_CUSTOMER_NAMES = ['測試客戶A', '測試客戶B', '測試客戶C', '測試客戶D', '測試客戶E']

FAKE_PRODUCTS = [
    ('狗飼料', 450.0),
    ('貓罐頭', 35.0),
    ('寵物玩具', 120.0),
    ('貓砂', 280.0),
    ('寵物零食', 90.0),
]


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    note_t = fields.Text(string='備註T')

    def _get_or_create_fake_partners(self):
        partners = self.env['res.partner'].search([('customer_rank', '>', 0)])
        if partners:
            return partners
        return self.env['res.partner'].create([{'name': name} for name in FAKE_CUSTOMER_NAMES])

    def _get_or_create_fake_products(self):
        products = self.env['product.product'].search([('sale_ok', '=', True)])
        if products:
            return products
        return self.env['product.product'].create([
            {'name': name, 'list_price': price, 'sale_ok': True}
            for name, price in FAKE_PRODUCTS
        ])

    def action_generate_fake_quotations(self):
        partners = self._get_or_create_fake_partners()
        products = self._get_or_create_fake_products()
        now = fields.Datetime.now()
        orders_vals = []
        for i in range(50):
            order_lines = [(0, 0, {
                'product_id': random.choice(products).id,
                'product_uom_qty': random.randint(1, 10),
            }) for _line in range(random.randint(1, 5))]
            orders_vals.append({
                'partner_id': random.choice(partners).id,
                'date_order': now - timedelta(days=random.randint(0, 90), hours=random.randint(0, 23)),
                'note_t': f'自動產生測試備註 #{i + 1}',
                'order_line': order_lines,
            })
        self.env['sale.order'].create(orders_vals)
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': '測試資料已產生',
                'message': '已成功產生 50 筆測試報價單',
                'type': 'success',
                'sticky': False,
            },
        }
