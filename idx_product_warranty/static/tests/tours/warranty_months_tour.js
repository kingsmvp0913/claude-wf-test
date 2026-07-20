/** @odoo-module **/

import { registry } from "@web/core/registry";

registry.category("web_tour.tours").add("idx_product_warranty_tour", {
    url: "/web",
    test: true,
    steps: () => [
        {
            trigger: ".o_field_widget[name='warranty_months'] input:value(0)",
            content: "確認一般資訊頁籤可見保固月數欄位，預設值為 0",
        },
        {
            trigger: ".o_field_widget[name='warranty_months'] input",
            content: "輸入保固月數 12",
            run: "edit 12",
        },
        {
            trigger: ".o_form_button_save",
            content: "儲存產品表單",
            run: "click",
        },
        {
            trigger: ".o_field_widget[name='warranty_months'] input:value(12)",
            content: "確認保固月數已成功儲存為 12",
        },
    ],
});

registry.category("web_tour.tours").add("idx_product_warranty_reload_tour", {
    url: "/web",
    test: true,
    steps: () => [
        {
            trigger: ".o_field_widget[name='warranty_months'] input:value(12)",
            content: "重新載入該產品表單，確認保固月數欄位值仍為 12",
        },
    ],
});
