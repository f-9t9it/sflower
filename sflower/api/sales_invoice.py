from __future__ import unicode_literals
import json
import frappe
from frappe.utils import nowdate, nowtime, cint
from toolz import compose, unique, partial
from erpnext.accounts.doctype.sales_invoice.sales_invoice import make_delivery_note


@frappe.whitelist()
def deliver_qol(name, payments, deliver):
    is_delivery = cint(deliver)

    def make_payment(payment):
        pe = _make_payment_entry(
            name,
            payment.get('mode_of_payment'),
            payment.get('amount')
        )
        pe.insert(ignore_permissions=True)
        pe.submit()

    if payments:
        payments_list = json.loads(payments)
        map(make_payment, payments_list)

    if is_delivery:
        dn = make_delivery_note(name)
        dn.insert(ignore_permissions=True)
        dn.submit()


def _make_payment_entry(name, mode_of_payment, paid_amount):
    si = frappe.get_doc('Sales Invoice', name)
    payment_account = _get_account(mode_of_payment, si.company)
    pe = frappe.new_doc('Payment Entry')
    pe.update({
        'payment_type': 'Receive',
        'posting_date': nowdate(),
        'posting_time': nowtime(),
        'company': si.company,
        'mode_of_payment': mode_of_payment,
        'paid_amount': paid_amount,
        'received_amount': paid_amount,
        'allocate_payment_amount': 1,
        'party_type': 'Customer',
        'party': si.customer,
        'paid_from': si.debit_to,
        'paid_to': payment_account.name
    })
    pe.append('references', {
        'reference_doctype': 'Sales Invoice',
        'reference_name': name,
        'allocated_amount': paid_amount
    })
    pe.setup_party_account_field()
    pe.set_missing_values()
    return pe


@frappe.whitelist()
def get_ref_so_statuses(sales_invoice):
    get_statuses = compose(

        partial(map, lambda x: frappe.db.get_value('Sales Order', x, 'status')),
        _get_sales_orders
    )
    return get_statuses(sales_invoice)


def _get_sales_orders(sales_invoice):
    doc = frappe.get_doc('Sales Invoice', sales_invoice)
    get_so_names = compose(
        list,
        unique,
        partial(map, lambda x: x.sales_order)
    )
    return get_so_names(doc.items)


def _get_account(mode_of_payment, company):
    mopa = frappe.db.exists(
        'Mode of Payment Account', {'parent': mode_of_payment, 'company': company}
    )
    account = frappe.db.get_value('Mode of Payment Account', mopa, 'default_account')
    return frappe.get_doc('Account', account)
