from ninja import Router
from .schemas import UserSchema
from .models import User
from django.contrib.auth.hashers import make_password # hash para senhas
from django.core.exceptions import ValidationError
from rolepermissions.roles import assign_role

users_router = Router()

@users_router.post('/', response={200: dict, 400: dict})
def create_user(request, type_user_schema: UserSchema):
    user = User(**user.dict())
    user.password = make_password(user.password)
    try:
        user.full_clean()
        user.save()
        assign_role(user,)
    except ValidationError as e:
        return 400, {'error': e.message_dict}
    except Exception as e:
        return 500, {'error': 'Erro interno do sistema, contate um adm'}
    return {'ok': True}

