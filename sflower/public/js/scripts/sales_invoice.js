import DeliverDialog from '../frappe-components/DeliverDialog';

function _render_payment_button(frm) {
    frm.add_custom_button(__('Print Invoice'), function() {
        frm.deliver_dialog && frm.deliver_dialog.payment_and_deliver(frm);
    });
}

export default {
    setup: function(frm) {
        frm.deliver_dialog = new DeliverDialog();
    },
    refresh: function(frm) {
        _render_payment_button(frm);
    }
};
