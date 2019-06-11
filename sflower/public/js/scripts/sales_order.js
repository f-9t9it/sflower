import InvoiceDialog from '../frappe-components/InvoiceDialog';

function _render_invoice_button(frm) {
    // from erpnext/selling/doctype/sales_order/sales_order.js
    // erpnext/controllers/status_updater.py
    if (frm.doc.docstatus === 1 && frm.doc.status !== 'Closed') {
        if (flt(frm.doc.per_billed, 6) < 100) {
            frm.add_custom_button(__('Invoice & Print'), function() {
               frm.invoice_dialog && frm.invoice_dialog.create_and_print(frm);
            });
        } else {
            frm.add_custom_button(__('Print Invoice'), function() {
                frm.invoice_dialog && frm.invoice_dialog.print(frm);
            });
        }
    }
}

function _rename_delivery_fields(frm) {
    let date_label = "Delivery Date";
    let time_label = "Delivery Time";

    if (frm.doc.sf_order_type === "Collection") {
        date_label = "Collection Date";
        time_label = "Collection Time";
    }

    frm.set_df_property('delivery_date', 'label', __(date_label));
    frm.set_df_property('sf_delivery_time', 'label', __(time_label));
}

export default {
    setup: async function(frm) {
        const { pos_mop, order_pfs } = await frappe.db.get_doc('SF Settings');
        frm.invoice_dialog = new InvoiceDialog(pos_mop, order_pfs);
    },
    refresh: function(frm) {
        _render_invoice_button(frm);
    },
    sf_order_type: function(frm) {
        _rename_delivery_fields(frm);
    }
};
