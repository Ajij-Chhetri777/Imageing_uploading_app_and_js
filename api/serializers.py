from theapp.models import Thepost, Comment, Type
from rest_framework import serializers

class  Thepostserializer(serializers.ModelSerializer):
    class Meta:
        model = Thepost
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'