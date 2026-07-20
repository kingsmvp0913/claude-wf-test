/** @odoo-module **/

import { registry } from "@web/core/registry";

registry.category("web_tour.tours").add("idx_partner_sales_rep_sale_order_tour", {
    url: "/odoo",
    test: true,
    steps: () => [
        {
            trigger: '.o_app[data-menu-xmlid="sale.sale_menu_root"]',
            content: "開啟銷售 App",
        },
        {
            trigger: ".o_list_button_add",
            content: "新增報價單",
        },
        {
            trigger: '.o_field_widget[name="partner_id"] input',
            run: "text TourE2E Partner WithRep",
        },
        {
            trigger: '.ui-menu-item > a:contains("TourE2E Partner WithRep")',
        },
        {
            trigger: '.o_field_widget[name="user_id"] input:contains("TourE2E SalesRep Alpha")',
            content: "acceptance 2：已設業務負責人的客戶 → 銷售員自動帶入",
        },
        {
            trigger: '.o_field_widget[name="partner_id"] input',
            run: "text TourE2E Partner NoRep",
        },
        {
            trigger: '.ui-menu-item > a:contains("TourE2E Partner NoRep")',
        },
        {
            trigger: '.o_field_widget[name="user_id"] input:contains("TourE2E SalesRep Alpha")',
            content: "acceptance 3：未設業務負責人的客戶 → 銷售員維持原值不清空",
        },
        {
            trigger: '.o_field_widget[name="user_id"] input',
            run: "text TourE2E SalesRep Beta",
        },
        {
            trigger: '.ui-menu-item > a:contains("TourE2E SalesRep Beta")',
        },
        {
            trigger: ".o_form_button_save",
        },
        {
            trigger: "body:not(:has(.o_form_button_save))",
            run: function () {
                location.reload();
            },
        },
        {
            trigger: '.o_field_widget[name="user_id"] input:contains("TourE2E SalesRep Beta")',
            content: "acceptance 4：手動改選銷售員後，存檔重載仍保留手動選擇的值",
        },
    ],
});
