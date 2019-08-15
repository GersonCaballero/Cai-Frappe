# -*- coding: utf-8 -*-
# Copyright (c) 2019, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from datetime import datetime
from frappe.model.document import Document

class GCAI(Document):
    
    def validate(self):
        self.validate_range()
        self.validate_dates()
        self.validate_mask()
        self.generate_number()

    def validate_dates(self):
        if str(self.due_date) <= str(datetime.now()):
            frappe.throw(_("Date less than the current date."))

    def validate_range(self):
        if self.initial_range > self.final_range:
            frappe.throw(_("The initial range must be less than the final range"))
    
    def validate_mask(self):
        cai = self.cai

        segment = 6

        for i in range(4):
            if cai[segment] != "-":
                frappe.throw(_("CAI: There is a problem with segment {}".format(i+1)))
            
            segment = segment + 7
        
        if len(cai) > 37:
            frappe.throw(_("CAI: There are more written characters"))
    
    def initial_number(self, num):

        if num >= 1 and num < 10:
            return("0000000" + str(num))
        elif num >= 10 and num < 100:
            return("000000" + str(num))
        elif num >= 100 and num < 1000:
            return("00000"+ str(num))
        elif num >= 1000 and num < 10000:
            return("0000" + str(num))
        elif num >= 10000 and num < 100000:
            return("000" + str(num))
        elif num >= 100000 and num < 1000000:
            return("00" + str(num))
        elif num >= 1000000 and num < 10000000:
            return("0" + str(num))
        elif num >= 10000000:
            return(str(num))

    def generate_number(self):
        document = frappe.get_all("GType Document",["number"],filters = {"name": self.type_document})
        sucursal= frappe.get_all("GSucursal",["codigo"], filters = {"name": self.sucursal})
        pos = frappe.get_all("GPos",["codigo"], filters = {"name": self.pos_name})


        number = self.initial_number(self.initial_range)

        self.number = "{}-{}-{}-{}".format(sucursal[0].codigo, pos[0].codigo, document[0].number, number)
        
        if self.current_numbering is None:
            self.current_numbering = self.initial_range