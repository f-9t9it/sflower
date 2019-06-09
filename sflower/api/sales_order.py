from __future__ import unicode_literals

import json
import frappe
from erpnext.selling.doctype.sales_order.sales_order import make_sales_invoice


@frappe.whitelist()
def invoice_qol(name, payments):
    doc = make_sales_invoice(name)

    if payments:
        doc.is_pos = 1
        payments_list = json.loads(payments)
        map(lambda x: doc.append('payments', x), payments_list)

    doc.insert(ignore_permissions=True)
    doc.submit()
    return doc.name
