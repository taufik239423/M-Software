from odoo import models, fields, api, SUPERUSER_ID, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError
from datetime import datetime,date,timedelta
from dateutil.relativedelta import relativedelta

class ListBook(models.Model):
    _name = "list.book"

    title = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author', required=True)
    date_published = fields.Date('Date Published')
    nop = fields.Integer('Number Of Pages')
    tob = fields.Selection([('novel','Novel'),
                            ('doc','Documentation'),
                            ('other','Other')], string="Type Of Book")


