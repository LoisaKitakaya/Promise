import graphene
import graphql_jwt
import commerce.schema as commerce_schema

class Mutation(graphene.ObjectType):

    token_auth = graphql_jwt.ObtainJSONWebToken.Field()

    verify_token = graphql_jwt.Verify.Field()

    refresh_token = graphql_jwt.Refresh.Field()

    revoke_token = graphql_jwt.Revoke.Field()

class Query(commerce_schema.Query, graphene.ObjectType):

    pass

schema = graphene.Schema(mutation=Mutation, query=Query)