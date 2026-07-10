/** @odoo-module **/

import { registry } from "@web/core/registry";

registry.category("web_tour.tours").add("idx_sale_stats_tour", {
    url: "/odoo/sales",
    test: true,
    steps: () => [
        {
            trigger: ".o_quotation_stats_button",
            content: "點擊統計報表按鈕",
            run: "click",
        },
        {
            trigger: ".o_quotation_stats_dashboard select",
            content: "確認篩選區已載入",
        },
        {
            trigger: ".o_quotation_stats_dashboard table tbody tr td",
            content: "確認統計數字已顯示",
        },
    ],
});
