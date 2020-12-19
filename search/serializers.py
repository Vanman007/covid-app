from rest_framework import serializers
from django.contrib.auth.models import User
from search.models import CovidUser
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
import json
from search.documents import CovidUserDocument

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')


class CovidUserDocumentSerializer(DocumentSerializer):

    location = serializers.SerializerMethodField()

    class Meta(object):
        """Meta options."""

        # Specify the correspondent document class
        document = CovidUserDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'city',
            'address',
            'state_province',
            'country'
        )

    def get_location(self, obj):
        """Represent location value."""
        try:
            return obj.location.to_dict()
        except:
            return {}