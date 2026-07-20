from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    warranty_months = fields.Integer(string='保固月數', default=0)
