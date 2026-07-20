from odoo.tests import HttpCase, tagged


@tagged('post_install', '-at_install')
class TestProductWarranty(HttpCase):

    def setUp(self):
        super().setUp()
        self.product = self.env['product.template'].create({
            'name': '保固測試商品',
        })

    def _form_url(self):
        return f"/web#model=product.template&view_type=form&id={self.product.id}"

    def test_warranty_months_default_and_save_tour(self):
        self.start_tour(self._form_url(), 'idx_product_warranty_tour', login='auto_test_user')
        self.assertEqual(self.product.warranty_months, 12)

    def test_warranty_months_persist_after_reload_tour(self):
        self.product.warranty_months = 12
        self.start_tour(self._form_url(), 'idx_product_warranty_reload_tour', login='auto_test_user')
