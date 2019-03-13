from rest_framework import serializers

from djangoapp.gitapp.models import User, Repository


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = '__all__'
