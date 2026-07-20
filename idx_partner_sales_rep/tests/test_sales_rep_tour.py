from odoo.tests import HttpCase, tagged


@tagged('post_install', '-at_install')
class TestPartnerSalesRepTour(HttpCase):

    def setUp(self):
        super().setUp()
        group_user = self.env.ref('base.group_user')
        rep_user = self.env['res.users'].create({
            'name': 'TourE2E SalesRep Alpha',
            'login': 'toure2e_salesrep_alpha',
            'email': 'toure2e_salesrep_alpha@example.com',
            'groups_id': [(6, 0, [group_user.id])],
        })
        self.env['res.users'].create({
            'name': 'TourE2E SalesRep Beta',
            'login': 'toure2e_salesrep_beta',
            'email': 'toure2e_salesrep_beta@example.com',
            'groups_id': [(6, 0, [group_user.id])],
        })
        self.env['res.partner'].create({
            'name': 'TourE2E Partner FieldTest',
        })
        self.env['res.partner'].create({
            'name': 'TourE2E Partner WithRep',
            'sales_rep_id': rep_user.id,
        })
        self.env['res.partner'].create({
            'name': 'TourE2E Partner NoRep',
        })

    def test_partner_sales_rep_field_persists(self):
        self.start_tour('/odoo', 'idx_partner_sales_rep_partner_tour', login='auto_test_user')

    def test_sale_order_onchange_sales_rep(self):
        self.start_tour('/odoo', 'idx_partner_sales_rep_sale_order_tour', login='auto_test_user')
