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

    single_product = graphene.Field(ProductType, slug=graphene.String(required=True))

    def resolve_all_products(root, info):

        return Product.objects.all()

    def resolve_all_categories(root, info):

        return Category.objects.all()

    def resolve_all_collections(root, info):

        return Collection.objects.all()

    def resolve_single_product(root, info, slug):

        return Product.objects.get(slug=slug)   