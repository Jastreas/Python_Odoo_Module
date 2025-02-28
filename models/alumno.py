from odoo import models, fields

class Alumno(models.Model):
    _name = 'practicas.alumno'
    _description = 'Alumno'

    name = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    identificacion = fields.Char(string='Número de Identificación', required=True)
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    departamento_id = fields.Many2one('practicas.departamento', string='Departamento')
    grado_id = fields.Many2one('practicas.grado', string='Grado')
    curso = fields.Char(string='Curso')
    empresa_id = fields.Many2one('res.partner', string='Empresa', domain=[('is_company', '=', True)])
