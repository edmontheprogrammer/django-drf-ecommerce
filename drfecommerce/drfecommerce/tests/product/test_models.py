import pytest

# This line makes the database available for all the tests below.
pytestmark = pytest.mark.django_db


class TestCategoryModel:
    # Note 1: "category_factory" is the formatt for accessing the "CategoryFactory"
    # Factory created in the "factories.py" file
    def test_str_method(self, category_factory):
        # Arrange: we bring all the resources we need for the test

        # Act: perform an action on the code, the Category Factory
        x = category_factory(name="test_cat")

        # Assert / Verifiy: testing to make sure that the outputs of the action is
        #                   what's expected, testing the string method
        assert x.__str__() == "test_cat"


class TestBrandModel:
    def test_str_method(self, brand_factory):
        # Arrange
        # Act
        obj = brand_factory(name="test_brand")
        # Assert
        assert obj.__str__() == "test_brand"


class TestProductModel:
    def test_str_method(self, product_factory):
        # Arrange
        # Act
        obj = product_factory(name="test_product")
        # Assert
        assert obj.__str__() == "test_product"
