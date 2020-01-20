import graphene
from graphene_django.types import DjangoObjectType
from .models import Postingan

class PostinganType(DjangoObjectType):
    class Meta:
        model = Postingan

class Query(object):
    semua_postingan = graphene.List(PostinganType)

    def resolve_semua_postingan(self,info,**kwargs):
        return Postingan.objects.all()