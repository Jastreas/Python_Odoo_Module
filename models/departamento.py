from odoo import models, fields

class Departamento(models.Model):
    _name = 'practicas.departamento'
    _description = 'Departamento'

    name = fields.Char(string='Nombre', required=True)
    codigo = fields.Char(string='Código', required=True)
    director_id = fields.Many2one('res.users', string='Director')
