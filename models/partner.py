from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_client_status = fields.Selection([
        ('no', 'No ha sido cliente'),
        ('yes', 'Cliente actual'),
        ('former', 'Cliente anterior')
    ], string="Estado del Cliente")
