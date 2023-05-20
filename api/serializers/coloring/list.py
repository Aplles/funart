from rest_framework import serializers
from models_app.models import Coloring
from api.serializers.theme.list import ThemeListSerializer


class ColoringListSerializer(serializers.ModelSerializer):
    theme = ThemeListSerializer(read_only=True)

    class Meta:
        model = Coloring
        fields = (
            'id',
            'name',
            'image',
            'created_at',
            'updated_at',
            'type',
            'theme',
        )
