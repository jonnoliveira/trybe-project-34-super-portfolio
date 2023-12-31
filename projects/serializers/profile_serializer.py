from rest_framework import serializers
from projects.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "name", "github", "linkedin", "bio")
