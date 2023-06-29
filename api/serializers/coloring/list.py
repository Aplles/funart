from rest_framework import serializers
from models_app.models import Coloring
from api.serializers.theme.list import ThemeListSerializer


class ColoringListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coloring
        fields = (
            'id',
            'name',
            'image',
            'type',
        )
