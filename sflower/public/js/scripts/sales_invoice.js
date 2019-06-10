import DeliverDialog from '../frappe-components/DeliverDialog';

async function _render_payment_button(frm) {
    if (frm.doc.docstatus === 1) {
        const { status } = frm.doc;
        const { message: so_statuses = [] } = await frappe.call({
            method: 'sflower.api.sales_invoice.get_ref_so_statuses',
            args: {sales_invoice: frm.doc.name}
        });

        const can_be_paid = ['Unpaid', 'Overdue'].includes(status);

        frm.add_custom_button(__('Collect Order'), function () {
            const deliver = true;
            frm.deliver_dialog && frm.deliver_dialog.payment_and_deliver(frm, deliver);
        });
    }
}

export default {
    setup: async function(frm) {
        const { pos_mop, invoice_pfs } = await frappe.db.get_doc('SF Settings');
        frm.deliver_dialog = new DeliverDialog(pos_mop, invoice_pfs);
    },
    refresh: function(frm) {
        _render_payment_button(frm);
    }
};
