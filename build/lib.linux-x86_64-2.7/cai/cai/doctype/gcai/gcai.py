# -*- coding: utf-8 -*-
# Copyright (c) 2019, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class GCAI(Document):
    	def number(self):

            store_number = frappe.model.getvalue("store_number")

            pos_number = frappe.model.getvalue("pos_number")

            type_document = frappe.model.getvalue("type_document")

            initial_range = frappe.model.getvalue("initial_range")

            number = "{}-{}-{}-{}".format(store_number, pos_number, type_document, initial_range)

            frappe.model.set_value