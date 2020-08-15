from rest_framework import serializers
from .models import HotNews, TechnicalArticle


class HotNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotNews
        fields = "__all__"


class TechnicalArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalArticle
        fields = "__all__"
