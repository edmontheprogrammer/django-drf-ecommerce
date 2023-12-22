from pytest_factoryboy import register


from .factories import CategoryFactory, BrandFactory, ProductFactory

# This line registers the "CategoryFactory" factory into "pytest" and makes it
# available
register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)

# This is how to access the "CategoryFactory" using "category_factory"
# category_factory
# brand_factory
# product_factory
