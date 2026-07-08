/** @odoo-module **/

import { registry } from "@web/core/registry";

registry.category("web_tour.tours").add("idx_sale_note_t_tour", {
    url: "/odoo/sales",
    test: true,
    steps: () => [
        {
            trigger: ".o_list_button_add",
            content: "建立新報價單",
            run: "click",
        },
        {
            trigger: ".o_field_widget[name='partner_id'] input",
            content: "輸入客戶名稱",
            run: "edit Note T 測試客戶",
        },
        {
            trigger: ".o-autocomplete--dropdown-menu li:contains('Note T 測試客戶')",
            content: "選擇客戶",
            run: "click",
        },
        {
            trigger: ".o_field_widget[name='note_t'] textarea",
            content: "確認備註T欄位顯示於客戶欄位之後，並輸入備註內容",
            run: "edit 備註T自動化測試內容",
        },
        {
            trigger: ".o_form_button_save",
            content: "儲存報價單",
            run: "click",
        },
        {
            trigger: ".o_field_widget[name='note_t'] textarea:value(備註T自動化測試內容)",
            content: "確認備註T內容已成功儲存",
        },
    ],
});
