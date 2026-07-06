from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    note_t = fields.Text(string='備註T')
