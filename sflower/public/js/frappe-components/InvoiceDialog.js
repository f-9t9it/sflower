function _generate_pfs(pf) {
    return {
        fieldtype: 'Check',
        fieldname: pf,
        label: __(pf),
        default: 1
    };
};

export default class InvoiceDialog {
    constructor(pos_mop, print_formats = []) {
        this.mode_of_payments = [
            { mode_of_payment: pos_mop, amount: 0.00 }
        ];
        this.print_formats = print_formats;
        this.dialog = new frappe.ui.Dialog({
            title: 'Invoice & Print',
            fields: [
                {
                    fieldname: 'make_payment',
                    fieldtype: 'Check',
                    label: __('Make Payment'),
                    default: 1,
                    onchange: function(e) {
                        const make_payment = this.dialog.get_value('make_payment');
                        this.dialog.set_df_property('payments', 'hidden', !make_payment);
                    }.bind(this)
                },
                {
                    fieldname: 'payments',
                    fieldtype: 'Table',
                    fields: [
                        {
                            fieldname: 'mode_of_payment',
                            fieldtype: 'Link',
                            options: 'Mode of Payment',
                            label: __('Mode of Payment'),
                            in_list_view: 1
                        },
                        {
                            fieldname: 'amount',
                            fieldtype: 'Currency',
                            label: __('Amount'),
                            in_list_view: 1
                        }
                    ],
                    in_place_edit: true,
                    data: this.mode_of_payments,
                    get_data: () => this.mode_of_payments
                },
                {
                    fieldname: 'print_sb',
                    fieldtype: 'Section Break',
                    label: __('Print Formats')
                },
                ...this.print_formats.map(_generate_pfs)
            ]
        });
    }
    async create_and_print(frm) {
        this.dialog.get_primary_btn().off('click');
        this.dialog.set_primary_action(
            'OK',
            async function() {
                const { name } = frm.doc;
                const values = this.dialog.get_values();
                const payments = values.payments.map(({ mode_of_payment, amount }) => ({
                    mode_of_payment,
                    amount,
                }));
                this.dialog.hide();
                await frappe.call({
                    method: 'sflower.api.sales_order.invoice_qol',
                    freeze: true,
                    freeze_message: __('Creating Sales Invoice'),
                    args: { name, payments }
                });
                frm.reload_doc();
            }.bind(this)
        );
        this.dialog.show();
    }
    async print(frm) {
        const print_formats = this.print_formats;
        this.dialog.get_primary_btn().off('click');
        this.dialog.set_primary_action('OK', async function() {
            const { name } = frm.doc;
            const values = this.get_values();
            this.hide();
        });
        this.dialog.show();
    }
}