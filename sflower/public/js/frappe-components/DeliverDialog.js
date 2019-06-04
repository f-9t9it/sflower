export default class DeliverDialog {
    constructor() {
        this.dialog = new frappe.ui.Dialog({
            title: 'Deliver & Print',
            fields: [
                {
                    fieldname: 'test',
                    fieldtype: 'Check',
                    label: __('Test')
                }
            ]
        });
    }
    payment_and_deliver(frm) {
        this.dialog.show();
    }
}