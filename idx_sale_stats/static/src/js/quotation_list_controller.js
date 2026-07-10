/** @odoo-module **/

import { registry } from "@web/core/registry";
import { listView } from "@web/views/list/list_view";
import { ListController } from "@web/views/list/list_controller";
import { useService } from "@web/core/utils/hooks";

export class QuotationStatsListController extends ListController {
    setup() {
        super.setup();
        this.actionService = useService("action");
    }

    async onOpenQuotationStats() {
        await this.actionService.doAction("idx_sale_stats.action_quotation_stats_dashboard");
    }
}

registry.category("views").add("sale_quotation_stats_list", {
    ...listView,
    Controller: QuotationStatsListController,
    buttonTemplate: "idx_sale_stats.ListView.Buttons",
});
