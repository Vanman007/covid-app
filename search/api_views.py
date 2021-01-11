from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_GEO_DISTANCE,
    SUGGESTER_COMPLETION
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend,
    DefaultOrderingFilterBackend,
    SuggesterFilterBackend,
    NestedFilteringFilterBackend,
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
        DefaultOrderingFilterBackend,
        CompoundSearchFilterBackend,
        SuggesterFilterBackend,

    ]
    pagination_class = LimitOffsetPagination
    # Define search fields
    search_fields = (
        'city.name',
        'city.country.name',
    )
    # Define filtering fields
    filter_fields = {
        'id': None,
        'city': 'city.name.raw',        
    }
    # Specify default ordering
    ordering_fields = {
        'id': None,
        'street': None,
        'city': 'city.name.raw',
    }    
    ordering = {
        'id': None,
        'city.name.raw': None,
    }
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
            'field': 'city.name.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
            # 'options': {
            #     'size': 6,  # Override default number of suggestions
            #     'skip_duplicates':True, # Whether duplicate suggestions should be filtered out.
            # },
        },
        'country_suggest': {
            'field': 'country.name.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        },
    }
