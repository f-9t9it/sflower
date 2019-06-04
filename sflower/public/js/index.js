import { sales_order, sales_invoice } from './scripts';

frappe.ui.form.on('Sales Order', sales_order);
frappe.ui.form.on('Sales Invoice', sales_invoice);