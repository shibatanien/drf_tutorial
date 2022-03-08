from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Drink
        fields = ['id', 'name', 'price', 'created', 'owner']

class UserSerializer(serializers.ModelSerializer):
    # Drink is a reverse relationship on the User model, it will not be included by default when using ModelSerializer
    # so we need to add an explicit field for it
    drinks = serializers.PrimaryKeyRelatedField(many=True, queryset=Drink.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'drinks']