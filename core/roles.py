from rolepermissions.roles import AbstractUserRole


class PeopleRole(AbstractUserRole):
    available_permissions = {
        'make_transfer': True,
        'receive_transfer': True
    }
    
class CompanyRole(AbstractUserRole):
        available_permissions = {
        'make_transfer': False,
        'receive_transfer': True
    }
    