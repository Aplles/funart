from rest_framework import serializers
from models_app.models import Theme


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = (
            'id',
            'name',
            'description',
            'created_at',
            'updated_at',
        )
