import graphene
import Postingan.schema as sc
import Blogger.user.schema as userSc

class Mutation(userSc.Mutation,sc.Mutation, graphene.ObjectType):
    pass

class Query(sc.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)