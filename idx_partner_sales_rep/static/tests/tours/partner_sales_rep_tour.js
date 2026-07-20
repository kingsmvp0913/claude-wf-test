/** @odoo-module **/

import { registry } from "@web/core/registry";

registry.category("web_tour.tours").add("idx_partner_sales_rep_partner_tour", {
    url: "/odoo",
    test: true,
    steps: () => [
        {
            trigger: '.o_app[data-menu-xmlid="contacts.menu_contacts"]',
            content: "開啟聯絡人 App",
        },
        {
            trigger: ".o_searchview_input",
            run: "text TourE2E Partner FieldTest",
        },
        {
            trigger: ".o_searchview_input",
            run: "press Enter",
        },
        {
            trigger: '.o_kanban_record:contains("TourE2E Partner FieldTest")',
            content: "打開待測客戶",
        },
        {
            trigger: '.o_notebook .nav-link:contains("Sales")',
            content: "切到「銷售與採購」頁籤",
        },
        {
            trigger: '.o_field_widget[name="sales_rep_id"] input',
            run: "text TourE2E SalesRep Alpha",
        },
        {
            trigger: '.ui-menu-item > a:contains("TourE2E SalesRep Alpha")',
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
            trigger: '.o_notebook .nav-link:contains("Sales")',
        },
        {
            trigger: '.o_field_widget[name="sales_rep_id"] input:contains("TourE2E SalesRep Alpha")',
            content: "acceptance 1：業務負責人存檔重載後仍保留",
        },
    ],
});
