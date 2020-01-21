import graphene
import graphql_jwt
import Postingan.schema as sc
import Blogger.user.schema as userSc

class Mutation(userSc.Mutation,sc.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

class Query(userSc.Query,sc.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)