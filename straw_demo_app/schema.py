import strawberry
from strawberry_django_jwt.middleware import JSONWebTokenMiddleware, AsyncJSONWebTokenMiddleware
import strawberry_django_jwt.mutations as jwt_mutations
from strawberry.types import Info
from strawberry_django_jwt.decorators import login_required
from strawberry_django_jwt.decorators import login_field

from typing import List
from .types import Color, Fruit


@strawberry.type
class Query:

    @login_field
    def hello(self, info: Info) -> str:
        # print(self)
        # print(info)
        return "World %s" % info.context.request.user.email

    # fruits: List[Fruit] = strawberry.django.field()
    colors: List[Color] = strawberry.django.field()

@strawberry.type
class Mutation:
    token_auth = jwt_mutations.ObtainJSONWebToken.obtain
    verify_token = jwt_mutations.Verify.verify
    refresh_token = jwt_mutations.Refresh.refresh
    delete_token_cookie = jwt_mutations.DeleteJSONWebTokenCookie.delete_cookie

schema = strawberry.Schema(query=Query, mutation=Mutation, extensions=[JSONWebTokenMiddleware,])