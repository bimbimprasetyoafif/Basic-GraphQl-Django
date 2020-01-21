import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Postingan

class PostinganType(DjangoObjectType):
    class Meta:
        model = Postingan
        filter_fields = ('id','judul')
        interfaces = (graphene.relay.Node,)

class CreatePostingan(graphene.relay.ClientIDMutation):
    post = graphene.Field(PostinganType)
    class Input:
        judul = graphene.String()
        isi = graphene.String()
    
    @classmethod
    def mutate_and_get_payload(self, root, info, **input):
        judul = input.get('judul')
        isi = input.get('isi')

        postingan = Postingan(
            judul=judul,
            isi=isi
        )
        postingan.save()

        return CreatePostingan(post = postingan)
        
class UpdatePostingan(graphene.relay.ClientIDMutation):
    post = graphene.Field(PostinganType)
    class Input:
        id = graphene.String()
        judul = graphene.String()
        isi = graphene.String()
    
    @classmethod
    def mutate_and_get_payload(self, root, info, **input):
        judul = input.get('judul')
        isi = input.get('isi')
        id = input.get('id')
        id = graphene.relay.Node.from_global_id(id)[1]

        postingan = Postingan.objects.get(id=id)
        postingan.judul = judul
        postingan.isi = isi
        postingan.save()

        return UpdatePostingan(post = postingan)

class DeletePostingan(graphene.relay.ClientIDMutation):
    post = graphene.Field(PostinganType)
    ok = graphene.Boolean()
    ok = False
    class Input:
        id = graphene.String()
    
    @classmethod
    def mutate_and_get_payload(self, root, info, **input):
        id = input.get('id')
        id = graphene.relay.Node.from_global_id(id)[1]
        try:
            postingan = Postingan.objects.get(id=id)
            postingan.delete()
            this.ok = True
            return DeletePostingan(ok)
        except:
            return DeletePostingan(ok)

class RelayMutation(graphene.AbstractType):
    tambah_postingan = CreatePostingan.Field()
    update_postingan = UpdatePostingan.Field()
    delete_postingan = DeletePostingan.Field()

class Query(object):
    postingan = graphene.relay.Node.Field(PostinganType)
    semua_postingan = DjangoFilterConnectionField(PostinganType)