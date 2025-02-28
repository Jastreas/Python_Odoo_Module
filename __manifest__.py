{
    'name': 'Prácticas Alumnos',
    'version': '1.1',
    'summary': 'Gestión de prácticas de alumnos',
    'description': 'Módulo para gestionar la asignación de prácticas a alumnos en empresas.',
    'author': 'Juan Andreas Manea',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/departamento_views.xml',
        'views/grado_views.xml',
        'views/alumno_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
}
