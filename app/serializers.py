from rest_framework import serializers
from .models import Player

# 1. lets make a serializer class that converts Player model to Json, takes jscon and creates /updes Player model
class PlayerSerializer(serializers.ModelSerializer):
    # this nested class gives django rest framewrk metadeta we want to serialize
    class Meta:
        # use the player model from models.py
        model = Player
        # now include all feilds from the player model in the json
        fields = '__all__'
    # You could also manually pick specific fields like this:  fields = ['id', 'name', 'position']
    #