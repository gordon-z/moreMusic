from rest_framework import serializers
from .models import Recommendation, Track
from django.contrib.auth.models import User

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['track_id', 'track_name', 'track_uri', 'album_name', 'album_art', 'album_release_date', 'artist_id', 'artist_name', 'artist_uri']

class RecommendationSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = ['user', 'title', 'timestamp']
        extra_kwargs = {"user": {"read_only": True}}

class RecommendationSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)
    
    class Meta:
        model = Recommendation
        fields = ['user', 'title', 'tracks', 'timestamp']
        extra_kwargs = {"user": {"read_only": True}}

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user