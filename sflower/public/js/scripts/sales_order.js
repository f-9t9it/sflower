function _render_invoice_button(frm) {
    frm.add_custom_button(__('Print Invoice'), function() {
        console.log("Initial Print Invoice");
    });
}

export default {
    refresh: function(frm) {
        _render_invoice_button(frm);
    }
};
