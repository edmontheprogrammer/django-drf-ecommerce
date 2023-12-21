from pytest_factoryboy import register


from .factories import CategoryFactory

# This line registers the "CategoryFactory" factory into "pytest" and makes it
# available
register(CategoryFactory)

# This is how to access the "CategoryFactory" using "category_factory"
category_factory
