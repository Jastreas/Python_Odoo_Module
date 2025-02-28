from odoo import models, fields

class Grado(models.Model):
    _name = 'practicas.grado'
    _description = 'Grado'

    name = fields.Char(string='Nombre', required=True)
    codigo = fields.Char(string='Código', required=True)
    tutor_id = fields.Many2one('res.users', string='Tutor')
    departamento_id = fields.Many2one('practicas.departamento', string='Departamento')
