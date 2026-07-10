from odoo import api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def get_quotation_stats(self, domain=None):
        domain = domain or []
        order_groups = self.read_group(domain, ['amount_total:sum'], ['partner_id'])
        orders = self.search(domain)
        line_groups = self.env['sale.order.line'].read_group(
            [('order_id', 'in', orders.ids)], [], ['order_partner_id']
        )
        item_count_by_partner = {
            group['order_partner_id'][0]: group.get('__count', group.get('order_partner_id_count', 0))
            for group in line_groups if group.get('order_partner_id')
        }
        total_orders = sum(
            group.get('__count', group.get('partner_id_count', 0)) for group in order_groups
        )

        stats = []
        for group in order_groups:
            partner = group.get('partner_id')
            if not partner:
                continue
            partner_id, partner_name = partner
            order_count = group.get('__count', group.get('partner_id_count', 0))
            stats.append({
                'partner_id': partner_id,
                'partner_name': partner_name,
                'amount_total': group.get('amount_total', 0.0),
                'item_count': item_count_by_partner.get(partner_id, 0),
                'order_count': order_count,
                'percentage': (order_count / total_orders * 100.0) if total_orders else 0.0,
            })
        return stats
