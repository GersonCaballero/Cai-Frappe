from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("CAI"),
        "icon": "octicon octicon-briefcase",
        "items": [
            {
              "type": "doctype",
              "name": "GCAI",
              "label": _("GCAI"),
              "description": _("This doctype is for create new CAIs."),
            }
          ]
      }
  ]

