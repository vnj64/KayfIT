"""Module used in REST API."""
from rest_framework import serializers

from .models import Product, Menu, Client, Order

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.second_name = validated_data.get("second_name", instance.second_name)
        instance.address = validated_data.get("address", instance.address)
        instance.phone_number = validated_data.get("phone_number", instance.phone_number)
        instance.age = validated_data.get("age", instance.age)
        instance.save()
        return instance

    def delete(self, validated_data):
        return Client.objects.delete(**validated_data)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
    
    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.menu_id = validated_data.get("menu_id", instance.menu_id)
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.descrpition)
        instance.image = validated_data.get("image", instance.image)
        instance.price = validated_data.get("price", instance.price)
        instance.url = validated_data.get("url", instance.url)
        instance.save()
        return instance

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"

    def create(self, validated_data):
        return Menu.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.restriction_age = validated_data.get("restriction_age", instance.restriction_age)
        instance.save()
        return instance

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.client_id = validated_data.get("client_id", instance.client_id)
        instance.orderstates = validated_data.get("orderstates", instance.orderstates)
        instance.important = validated_data.get("important", instance.important)
        instance.created = validated_data.get("created", instance.create)
        instance.save()
        return instance
        