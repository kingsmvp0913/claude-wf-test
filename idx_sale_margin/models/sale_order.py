from decimal import Decimal, ROUND_HALF_UP

from odoo import api, fields, models

MARGIN_RATE_QUANTIZER = Decimal('0.0001')


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    gross_margin_total = fields.Monetary(
        string='總毛利',
        compute='_compute_gross_margin',
        currency_field='currency_id',
    )
    margin_rate = fields.Float(
        string='毛利率',
        compute='_compute_gross_margin',
    )

    @api.depends('order_line.price_subtotal', 'order_line.product_uom_qty', 'order_line.product_id', 'amount_untaxed')
    def _compute_gross_margin(self):
        for order in self:
            decimal_places = order.currency_id.decimal_places or 2
            amount_quantizer = Decimal('1').scaleb(-decimal_places)
            total_margin = Decimal('0')
            for line in order.order_line:
                if not line.product_id:
                    continue
                cost = Decimal(str(line.product_id.standard_price)) * Decimal(str(line.product_uom_qty))
                subtotal = Decimal(str(line.price_subtotal))
                line_margin = (subtotal - cost).quantize(amount_quantizer, rounding=ROUND_HALF_UP)
                total_margin += line_margin
            order.gross_margin_total = float(total_margin)
            if order.amount_untaxed:
                rate = (total_margin / Decimal(str(order.amount_untaxed))).quantize(
                    MARGIN_RATE_QUANTIZER, rounding=ROUND_HALF_UP
                )
                order.margin_rate = float(rate)
            else:
                order.margin_rate = 0.0
