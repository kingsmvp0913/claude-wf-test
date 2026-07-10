/** @odoo-module **/

import { Component, useState, useRef, onWillStart, onMounted, onPatched } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { loadJS } from "@web/core/assets";

export class QuotationStatsDashboard extends Component {
    static template = "idx_sale_stats.QuotationStatsDashboard";

    setup() {
        this.orm = useService("orm");
        this.action = useService("action");
        this.chartRef = useRef("pieChart");
        this.pieChart = null;

        this.stateOptions = [
            { value: "draft", label: "報價單" },
            { value: "sent", label: "已寄送" },
            { value: "sale", label: "已確認" },
            { value: "done", label: "已鎖定" },
            { value: "cancel", label: "已取消" },
        ];

        this.state = useState({
            dateFrom: "",
            dateTo: "",
            states: [],
            partnerIds: [],
            partners: [],
            stats: [],
        });

        onWillStart(async () => {
            await loadJS("/web/static/lib/Chart/Chart.js");
            this.state.partners = await this.orm.searchRead("res.partner", [], ["id", "name"], { limit: 200 });
            await this.loadStats();
        });

        onMounted(() => this.renderPieChart());
        onPatched(() => this.renderPieChart());
    }

    getDomain() {
        const domain = [];
        if (this.state.dateFrom) {
            domain.push(["date_order", ">=", this.state.dateFrom]);
        }
        if (this.state.dateTo) {
            domain.push(["date_order", "<=", this.state.dateTo]);
        }
        if (this.state.states.length) {
            domain.push(["state", "in", this.state.states]);
        }
        if (this.state.partnerIds.length) {
            domain.push(["partner_id", "in", this.state.partnerIds]);
        }
        return domain;
    }

    async loadStats() {
        this.state.stats = await this.orm.call("sale.order", "get_quotation_stats", [this.getDomain()]);
    }

    async onStateChange(ev) {
        this.state.states = Array.from(ev.target.selectedOptions).map((o) => o.value);
        await this.loadStats();
    }

    async onPartnerChange(ev) {
        this.state.partnerIds = Array.from(ev.target.selectedOptions).map((o) => parseInt(o.value, 10));
        await this.loadStats();
    }

    async onFilterChange() {
        await this.loadStats();
    }

    renderPieChart() {
        if (!this.chartRef.el) {
            return;
        }
        const labels = this.state.stats.map((s) => s.partner_name);
        const data = this.state.stats.map((s) => s.order_count);
        if (this.pieChart) {
            this.pieChart.destroy();
        }
        this.pieChart = new Chart(this.chartRef.el, {
            type: "pie",
            data: {
                labels,
                datasets: [{
                    data,
                    backgroundColor: labels.map((label, i) => `hsl(${(i * 47) % 360}, 65%, 60%)`),
                }],
            },
            options: { responsive: true },
        });
    }

    async onExportPdf() {
        const domain = this.getDomain();
        const ids = await this.orm.search("sale.order", domain);
        await this.action.doAction("idx_sale_stats.action_report_quotation_stats", {
            additionalContext: { active_ids: ids },
        });
    }
}

registry.category("actions").add("idx_sale_stats.quotation_stats_dashboard", QuotationStatsDashboard);
