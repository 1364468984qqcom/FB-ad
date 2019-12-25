from rest_framework import serializers
from pic.models import Pic, Pic1


class PicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pic
        fields = ('created', 'pid', 'images')


class Pic1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pic1
        fields = ('pid', 'similar_rate', 'created')


class Pic2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pic1
        fields = ('similar_rate', 'created')
