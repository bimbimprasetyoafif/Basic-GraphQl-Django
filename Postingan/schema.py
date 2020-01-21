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
        
class UpdatePostingan(graphene.Mutation):
    id = graphene.Int()
    judul = graphene.String()
    isi = graphene.String()

    class Arguments:
        id = graphene.Int()
        judul = graphene.String()
        isi = graphene.String()
    
    def mutate(self,info,id,judul,isi):
        posting = Postingan.objects.get(pk=id)
        posting.judul = judul
        posting.isi = isi
        posting.save()

        return UpdatePostingan(
            id = posting.id,
            judul = posting.judul,
            isi = posting.isi
        )

class DeletePostingan(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.Int()
    
    def mutate(self,info,id):
        try:
            posting = Postingan.objects.get(pk=id)
            posting.delete()
            ok = True
        except:
            ok = False

        return DeletePostingan(ok)

class Mutation(object):
    tambah_postingan = CreatePostingan.Field()
    update_postingan = UpdatePostingan.Field()
    delete_postingan = DeletePostingan.Field()

class Query(object):
    semua_postingan = graphene.List(PostinganType)

    def resolve_semua_postingan(self,info,**kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in')
        return Postingan.objects.all()