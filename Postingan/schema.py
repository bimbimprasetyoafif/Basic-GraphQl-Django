import graphene
from graphene_django.types import DjangoObjectType
from .models import Postingan

class PostinganType(DjangoObjectType):
    class Meta:
        model = Postingan

class CreatePostingan(graphene.Mutation):
    id = graphene.Int()
    judul = graphene.String()
    isi = graphene.String()

    class Arguments:
        judul = graphene.String()
        isi = graphene.String()
    
    def mutate(self,info,judul,isi):
        posting = Postingan(
            judul = judul,
            isi = isi
        )
        posting.save()

        return CreatePostingan(
            id = posting.id,
            judul = posting.judul,
            isi = posting.isi
        )

class Mutation(object):
    tambah_postingan = CreatePostingan.Field()

class Query(object):
    semua_postingan = graphene.List(PostinganType)

    def resolve_semua_postingan(self,info,**kwargs):
        return Postingan.objects.all()