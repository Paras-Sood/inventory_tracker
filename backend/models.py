from django.db import models
from rest_framework.serializers import ModelSerializer

class Item(models.Model):
    name=models.CharField(max_length=200)
    price=models.DecimalField(decimal_places=2,max_digits=7)
    quantity=models.IntegerField()

    def __str__(self):
        return self.name

class ItemSerializer(ModelSerializer):
    class Meta:
        model=Item
        fields="__all__"
