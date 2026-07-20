from odoo import api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def _onchange_partner_id_sales_rep(self):
        if self.partner_id.sales_rep_id:
            self.user_id = self.partner_id.sales_rep_id
