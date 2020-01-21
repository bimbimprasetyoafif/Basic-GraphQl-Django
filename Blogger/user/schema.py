import graphene
from graphene_django.types import DjangoObjectType
from django.contrib.auth import get_user_model

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
    
    def mutate(self,info,email,username,password):
        user = get_user_model()(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)

class Mutation(object):
    create_user = CreateUser.Field()

class Query(object):
    user_type = graphene.List(UserType)
    me = graphene.Field(UserType)

    def resolve_me(self,info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in')
        return user

    def resolve_user_type(self,info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in')
        return get_user_model().objects.all()