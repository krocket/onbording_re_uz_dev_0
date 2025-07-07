{'name': 'Library Book Borrowing',
 'description': 'Members can borrow books from the library.',
 'author': 'Daniel Reis',
 'version': '18.0.0.1',
 'depends': [
     'library_member',
     'mail',
 ],
 'data': [
    'security/ir.model.access.csv',
    'views/library_menu.xml',
    'views/checkout_view.xml',
    'views/checkout_kanban_view.xml',
    'data/library_checkout_stage.xml',
    'wizard/checkout_mass_message_wizard.xml',
 ],
}
