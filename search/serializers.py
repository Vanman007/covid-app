from rest_framework import serializers
from django.contrib.auth.models import User
from search.models import CovidUser
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
import json
from search.documents import CovidUserDocument

# class CovidUserSerializer(serializers.Serializer):

#     city = serializers.CharField(read_only=True)
    
#     class Meta(object):
#         fields = ('city')

#     def validate(self, data):
#         if 'profile_picture' not in data:
#             raise ValidationError({'profile_picture': 'You need to add a profile picture'})
#         return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')

class CovidUserSerializer(DocumentSerializer):

  class Meta(object):
        """Meta options."""

        # Specify the correspondent document class
        document = CovidUserDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'city'
        )