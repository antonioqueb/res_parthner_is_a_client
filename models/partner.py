from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_is_a_client = fields.Boolean(string="Ha sido cliente en el pasado?")
