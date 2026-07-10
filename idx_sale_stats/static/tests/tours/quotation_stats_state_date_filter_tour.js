/** @odoo-module **/

import { registry } from "@web/core/registry";

registry.category("web_tour.tours").add("idx_sale_stats_state_filter_tour", {
    url: "/odoo/sales",
    test: true,
    steps: () => [
        {
            trigger: ".o_quotation_stats_button",
            content: "點擊統計報表按鈕",
            run: "click",
        },
        {
            trigger: "table tbody tr:contains('StatsStateCustomerConfirmed')",
            content: "確認已確認客戶資料列已顯示",
        },
        {
            trigger: "table tbody tr:contains('StatsStateCustomerOld')",
            content: "確認草稿客戶資料列已顯示",
        },
        {
            trigger: ".o_stats_filters > div:nth-child(3) select option:contains('已確認')",
            content: "篩選狀態為已確認",
            run: "click",
        },
        {
            trigger: "table tbody tr:only-child:contains('StatsStateCustomerConfirmed')",
            content: "確認篩選後僅剩已確認客戶資料列",
        },
    ],
});

registry.category("web_tour.tours").add("idx_sale_stats_date_filter_tour", {
    url: "/odoo/sales",
    test: true,
    steps: () => [
        {
            trigger: ".o_quotation_stats_button",
            content: "點擊統計報表按鈕",
            run: "click",
        },
        {
            trigger: "table tbody tr:contains('StatsStateCustomerConfirmed')",
            content: "確認近期報價單客戶資料列已顯示",
        },
        {
            trigger: "table tbody tr:contains('StatsStateCustomerOld')",
            content: "確認舊報價單客戶資料列已顯示",
        },
        {
            trigger: ".o_stats_filters > div:nth-child(1) input",
            content: "設定日期起篩選，排除舊報價單",
            run: "edit 2015-01-01",
        },
        {
            trigger: "table tbody tr:only-child:contains('StatsStateCustomerConfirmed')",
            content: "確認日期篩選後僅剩近期客戶資料列",
        },
    ],
});
