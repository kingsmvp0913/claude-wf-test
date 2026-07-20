from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    sales_rep_id = fields.Many2one('res.users', string='業務負責人')
