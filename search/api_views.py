# from rest_framework.generics import RetrieveUpdateDestroyAPIView
# from django.contrib.auth import get_user_model
# from rest_framework import permissions
# from .serializers import UserSerializer,CovidUserSerializer
# from search.documents import CovidUserDocument
# from elasticsearch_dsl import Search
# from search.models import CovidUser

# User = get_user_model()

# class CurrentUserUser(RetrieveUpdateDestroyAPIView):
#     queryset = User
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = UserSerializer

#     def get_object(self):
#         return self.request.user

#     def update(self, request, *args, **kwargs):
#         response = super().update(request, *args, **kwargs)
#         return response

#     def delete(self, request, *args, **kwargs):
#         user = self.get_object()
#         user.delete()
#         return Response(data='delete success')

# class sdCovidUser(RetrieveUpdateDestroyAPIView):
#     document = PostDocument 
#     queryset = CovidUser.objects.all()
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = CovidUserSerializer
#     search_fields = (
#         'city'
#     )

    
#     def get_object(self):
#         coviduser = PostDocument.search()
#         for hit in coviduser:
#             print(hit)
        
#         return coviduser

#     def update(self, request, *args, **kwargs):
#         response = super().update(request, *args, **kwargs)
#         return response

#     def delete(self, request, *args, **kwargs):
#         user = self.get_object()
#         user.delete()
#         return Response(data='delete success')

# # class CurrentUserViewSet(viewsets.ReadOnlyModelViewSet):
# #     queryset = User.objects.all()
# #     serializer_class = CurrentUserSerializer

from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_GEO_DISTANCE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    CompoundSearchFilterBackend,
    DefaultOrderingFilterBackend,
    SuggesterFilterBackend,
    FacetedSearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from search.documents import CovidUserDocument
from search.serializers import CovidUserDocumentSerializer

from django_elasticsearch_dsl_drf.constants import SUGGESTER_COMPLETION
from django_elasticsearch_dsl_drf.pagination import LimitOffsetPagination


class CovidUserDocumentView(DocumentViewSet):
    """The CovidUserDocument view."""

    document = CovidUserDocument
    serializer_class = CovidUserDocumentSerializer
    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        CompoundSearchFilterBackend,
        SuggesterFilterBackend,
    ]
    pagination_class = LimitOffsetPagination
    # Define search fields
    search_fields = (
        'address',
        'city',
        'state_province',
        'country',
    )
    # Define filtering fields
    filter_fields = {
        'id': None,
        'city': 'city.raw',
        'state_province': 'state_province.raw',
        'country': 'country.raw',
        'address':'address.raw',        
    }
    # Define ordering fields
    ordering_fields = {
        'id': None,
        'name': None,
        'city': None,
        'country': None,
        'address': None,
    }
    # Specify default ordering
    ordering = ('id')
    # Define geo-spatial filtering fields
    geo_spatial_filter_fields = {
        'location': {
            'lookups': [
                LOOKUP_FILTER_GEO_DISTANCE,
            ],
        },
    }
    suggester_fields = {
        'city_suggest': {
            'field': 'city.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
            'options': {
                'size': 6,  # Override default number of suggestions
                'skip_duplicates':True, # Whether duplicate suggestions should be filtered out.
            },
        },
        'state_province_suggest': {
            'field': 'state_province.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        },
        'country_suggest': {
            'field': 'country.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        },
        'address_suggest': {
            'field': 'address.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        },
        
    }
