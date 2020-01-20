import graphene
import Postingan.schema as sc

class Query(sc.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)