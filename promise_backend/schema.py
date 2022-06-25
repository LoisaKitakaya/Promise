import graphene
from graphene_django import DjangoObjectType
from users.models import User
import commerce.schema as commerce_schema

class UserType(DjangoObjectType):

    class Meta:

        model = User

        fields = '__all__'

class UserMutation(graphene.Mutation):

    class Arguments:

        username = graphene.String(required=True)

        email = graphene.String(required=True)

        first_name = graphene.String(required=True)

        last_name = graphene.String(required=True)

        password = graphene.String(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, username, email, first_name, last_name, password):

        user = User(username=username, email=email, first_name=first_name, last_name=last_name)

        user.set_password(password)

        user.save()

        return UserMutation(user=user)

class Mutation(graphene.ObjectType):

    create_user = UserMutation.Field()

class Query(commerce_schema.Query, graphene.ObjectType):

    all_users = graphene.List(UserType)

    def resolve_all_users(root, info):

        return User.objects.all()

schema = graphene.Schema(mutation=Mutation, query=Query)