# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "cai"
app_title = "CAI"
app_publisher = "Frappe"
app_description = "Este modulo es donde se crearan los CAIs para los distintios tipos de documentos que maneja la empresa."
app_icon = "oction oction-note"
app_color = "#589494 "
app_email = "gersoncaballero306@gmail.com"
app_license = "GNU Generil Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/cai/css/cai.css"
# app_include_js = "/assets/cai/js/cai.js"

# include js, css files in header of web template
# web_include_css = "/assets/cai/css/cai.css"
# web_include_js = "/assets/cai/js/cai.js"

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
# get_website_user_home_page = "cai.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "cai.install.before_install"
# after_install = "cai.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "cai.notifications.get_notification_config"

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
# 		"cai.tasks.all"
# 	],
# 	"daily": [
# 		"cai.tasks.daily"
# 	],
# 	"hourly": [
# 		"cai.tasks.hourly"
# 	],
# 	"weekly": [
# 		"cai.tasks.weekly"
# 	]
# 	"monthly": [
# 		"cai.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "cai.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "cai.event.get_events"
# }

