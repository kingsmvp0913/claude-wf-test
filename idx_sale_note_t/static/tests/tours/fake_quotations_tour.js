/** @odoo-module **/

import { registry } from "@web/core/registry";

registry.category("web_tour.tours").add("idx_sale_note_t_fake_data_tour", {
    url: "/odoo/sales",
    test: true,
    steps: () => [
        {
            trigger: "button[name='action_generate_fake_quotations']",
            content: "點擊「產生測試假資料」按鈕（第一次）",
            run: "click",
        },
        {
            trigger: ".o_notification_content:contains(已成功產生 50 筆測試報價單)",
            content: "確認第一次產生成功通知",
        },
        {
            trigger: "button[name='action_generate_fake_quotations']",
            content: "再次點擊「產生測試假資料」按鈕，驗證可重複觸發且不去重",
            run: "click",
        },
        {
            trigger: ".o_notification_content:contains(已成功產生 50 筆測試報價單)",
            content: "確認第二次產生成功通知",
        },
    ],
});
