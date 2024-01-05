from datetime import datetime
from rest_framework import serializers
from .models import Note
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    # shared_with = serializers.ListField(allow_empty=True, required=False)
    # child=serializers.CharField(),
    created_at = serializers.DateTimeField(default=datetime.now, read_only=True)

    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'owner', 'created_at']

    def create(self, validated_data):
        return Note.objects.create(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']