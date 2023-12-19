from rest_framework import serializers

from .models import Brand, Category, Product

# Note 1: You need two things to create "serializers" in Django: "serializers"
#           from the "rest_framework" and the "models"
# Note 2: Serializers allow complex data such as querysets and model instances
#  to be converted to native Python datatypes that can then be easily rendered
#  into JSON, XML or other content types. Serializers also provide deserialization,
#  allowing parsed data to be converted back into complex types,
#  after first validating the incoming data.


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"
