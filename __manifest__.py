{
    'name': 'Res Partner Is A Client',
    'version': '1.0',
    'category': 'Contacts',
    'summary': 'Extend Res Partner to indicate if they have been a client.',
    'depends': ['base', 'contacts'],  # Dependencias necesarias
    'data': [
        'views/partner_views.xml',  # Referencia a las vistas personalizadas
    ],
    'installable': True,
    'auto_install': False,
}
