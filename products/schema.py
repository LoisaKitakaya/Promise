import graphene
from graphene_django import DjangoObjectType
from .models import Product, Category, Collection, Currency

class ProductType(DjangoObjectType):

    class Meta:

        model = Product

        fields = '__all__'

class CategoryType(DjangoObjectType):

    class Meta:

        model = Category

        fields = '__all__'

class CollectionType(DjangoObjectType):

    class Meta:

        model = Collection

        fields = '__all__'

class CurrencyType(DjangoObjectType):

    class Meta:

        model = Currency

        fields = '__all__'

class Query(graphene.ObjectType):

    all_products = graphene.List(ProductType)

    all_categories = graphene.List(CategoryType)

    all_collections = graphene.List(CollectionType)

    def resolve_all_products(root, info):

        user = info.context.user

        if not user.is_authenticated:
            
            raise Exception("Authentication credentials were not provided")

        return Product.objects.all()

    def resolve_all_categories(root, info):

        user = info.context.user

        if not user.is_authenticated:

            raise Exception('Authentication credentials were not provided')

        return Category.objects.all()

    def resolve_all_collections(root, info):

        user = info.context.user

        if not user.is_authenticated:

            raise Exception('Authentication credentials were not provided')

        return Collection.objects.all()