from rest_framework import serializers
from models_app.models import Theme
from api.serializers.category.list import CategoryListSerializer


class ThemeListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer(read_only=False)

    class Meta:
        model = Theme
        fields = (
            'id',
            'name',
            'description',
            'image',
            'rating',
            'created_at',
            'updated_at',
            'category',
        )