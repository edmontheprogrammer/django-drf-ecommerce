import pytest
import json
pytestmark = pytest.mark.django_db


class TestCategoryEndpoints:
    # The Category Endpoint as listed in the browser
    endpoint = '/api/category/'

    # Testing a "Get Request" for viewing all Categories
    # in the Category endpoint
    # "api_client" is the pytest fixture, "api_client()" in "conftest.py" file.
    def test_category_get(self, category_factory, api_client):
        # Arrange : preparig the category endpoint
        category_factory.create_batch(4)

        # Act: Using the API-Client to make a call to the Get-Request
        response = api_client().get(self.endpoint)

        # Assert / Verifiy
        # "200" response is successful
        assert response.status_code == 200
        print(json.loads(response.content))
        assert len(json.loads(response.content)) == 4


class TestBrandEndpoints:
    # The Brand Endpoint as listed in the browser
    endpoint = '/api/brand/'

    # Testing a "Get Request" for viewing all brands
    # in the Brand endpoint
    # "api_client" is the pytest fixture, "api_client()" in "conftest.py" file.
    def test_brand_get(self, brand_factory, api_client):
        # Arrange : preparig the brand endpoint
        brand_factory.create_batch(4)

        # Act: Using the API-Client to make a call to the Get-Request
        response = api_client().get(self.endpoint)

        # Assert / Verifiy
        # "200" response is successful
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4


class TestProductEndpoints:
    # The Product Endpoint as listed in the browser
    endpoint = '/api/product/'

    # Testing a "Get Request" for viewing all Products
    # in the Product endpoint
    # "api_client" is the pytest fixture, "api_client()" in "conftest.py" file.
    def test_product_get(self, product_factory, api_client):
        # Arrange : preparig the product endpoint
        product_factory.create_batch(4)

        # Act: Using the API-Client to make a call to the Get-Request
        response = api_client().get(self.endpoint)

        # Assert / Verifiy
        # "200" response is successful
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4
