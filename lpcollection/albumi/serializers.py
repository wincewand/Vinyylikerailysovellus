from rest_framework import serializers
from .models import Albumi

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albumi
        fields = '__all__'