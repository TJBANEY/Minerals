from rest_framework import serializers

from . import models

class MineralSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mineral
        exclude = []