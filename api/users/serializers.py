from users.models import Profile
from django.contrib.auth.models import User
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'image']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    # TODO : fixing security problem with passwords in api
    #        api returns all passwords
    # TODO : fixing hashing problen with password creation with api
