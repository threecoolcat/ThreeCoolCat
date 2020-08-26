from rest_framework import serializers
from .models import HotNews, TechnicalArticle, FriendLinks, OperationLog


class HotNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotNews
        fields = "__all__"


class TechnicalArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalArticle
        fields = "__all__"


class FriendLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendLinks
        fields = "__all__"


class OperationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationLog
        fields = "__all__"
