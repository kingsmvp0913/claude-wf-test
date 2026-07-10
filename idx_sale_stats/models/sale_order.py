from odoo import api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def get_quotation_stats(self, domain=None):
        domain = domain or []
        order_groups = self.read_group(domain, ['amount_total:sum'], ['partner_id'])
        orders = self.search(domain)
        item_count_by_partner = {}
        for order in orders:
            partner_id = order.partner_id.id
            item_count_by_partner[partner_id] = (
                item_count_by_partner.get(partner_id, 0) + len(order.order_line)
            )
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
