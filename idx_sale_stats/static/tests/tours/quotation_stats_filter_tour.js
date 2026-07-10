/** @odoo-module **/

import { registry } from "@web/core/registry";

registry.category("web_tour.tours").add("idx_sale_stats_filter_tour", {
    url: "/odoo/sales",
    test: true,
    steps: () => [
        {
            trigger: ".o_quotation_stats_button",
            content: "點擊統計報表按鈕",
            run: "click",
        },
        {
            trigger: "table tbody tr:contains('StatsTourCustomerA')",
            content: "確認客戶A資料列已顯示",
        },
        {
            trigger: "table tbody tr:contains('StatsTourCustomerB')",
            content: "確認客戶B資料列已顯示",
        },
        {
            trigger: ".o_stats_filters > div:nth-child(4) select option:contains('StatsTourCustomerA')",
            content: "篩選客戶為客戶A",
            run: "click",
        },
        {
            trigger: "table tbody tr:only-child:contains('StatsTourCustomerA')",
            content: "確認篩選後僅剩客戶A資料列",
        },
        {
            trigger: "button:contains('匯出 PDF')",
            content: "點擊匯出PDF按鈕",
            run: "click",
        },
    ],
});
