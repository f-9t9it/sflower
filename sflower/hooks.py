# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "sflower"
app_title = "Singapore Flowers"
app_publisher = "9T9IT"
app_description = "ERPNext App for Singapore Flowers"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@9t9it.com"
app_license = "MIT"

fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
                    "Sales Invoice Item-sf_extra",
                    "Sales Invoice-sf_note_1",
                    "Sales Invoice-sf_card",
                    "Sales Order Item-sf_extra",
                    "Sales Order-sf_note_1",
                    "Sales Order-sf_card",
                    "Sales Invoice-sf_order_type",
                    "Sales Order-sf_delivery_time",
                    "Quotation-sf_occasion",
                    "Quotation-sf_events_section",
                    "Quotation-sf_event_time",
                    "Quotation-sf_set_up_time",
                    "Quotation-sf_events_column",
                    "Quotation-sf_breakdown_time",
                    "Quotation-sf_quotation_description",
                    "Quotation-sf_sales_type",
                    "Sales Order-sf_sales_type",
                    "Sales Invoice-sf_sales_type"
                ]
            ]
        ]
    },
    {
        "doctype": "Property Setter",
        "filters": [
            [
                "name",
                "in",
                [
                    "Sales Order-order_type-options"
                ]
            ]
        ]
    }
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sflower/css/sflower.css"
app_include_js = "/assets/js/sflower.min.js"

# include js, css files in header of web template
# web_include_css = "/assets/sflower/css/sflower.css"
# web_include_js = "/assets/sflower/js/sflower.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "sflower.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "sflower.install.before_install"
# after_install = "sflower.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sflower.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sflower.tasks.all"
# 	],
# 	"daily": [
# 		"sflower.tasks.daily"
# 	],
# 	"hourly": [
# 		"sflower.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sflower.tasks.weekly"
# 	]
# 	"monthly": [
# 		"sflower.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "sflower.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sflower.event.get_events"
# }

