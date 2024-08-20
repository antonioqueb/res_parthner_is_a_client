from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    x_is_a_client = fields.Boolean(string="Ha sido cliente en el pasado?")
    x_client_status = fields.Selection([
        ('no', 'No ha sido cliente'),
        ('yes', 'Cliente actual'),
        ('former', 'Cliente anterior')
    ], string="Estado del Cliente")
