import graphene
from graphene_django import DjangoObjectType
from .models import Product

class ProductType(DjangoObjectType):

    class Meta:

        model = Product

        fields = '__all__'

class Query(graphene.ObjectType):

    all_products = graphene.List(ProductType)

    def resolve_all_products(root, info):

        user = info.context.user

        if not user.is_authenticated:
            
            raise Exception("Authentication credentials were not provided")

        return Product.objects.all()