from odoo import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_test_button(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'type': 'warning',
                'message': '這是測試',
            },
        }
