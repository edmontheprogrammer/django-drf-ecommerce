import pytest
from pytest_factoryboy import register

from rest_framework.test import APIClient

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


@pytest.fixture
def api_client():
    return APIClient
