from odoo import api, models


class ReportQuotationStats(models.AbstractModel):
    _name = 'report.idx_sale_stats.report_quotation_stats_document'
    _description = 'Quotation Stats Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        stats = self.env['sale.order'].get_quotation_stats([('id', 'in', docids)])
        return {
            'doc_ids': docids,
            'doc_model': 'sale.order',
            'docs': self.env['sale.order'].browse(docids),
            'stats': stats,
        }
