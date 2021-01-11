from django.contrib.auth import get_user_model
from django_elasticsearch_dsl import Document, fields, Index
from django_elasticsearch_dsl.registries import registry
from .models import CovidUser
from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl_drf.compat import KeywordField, StringField

User = get_user_model()


SEARCH_INDEX = Index('search')

SEARCH_INDEX.settings(
    number_of_shards=3,
    number_of_replicas=2
)

@SEARCH_INDEX.doc_type
class CovidUserDocument(Document):
    id = fields.IntegerField(attr='id')

    user = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'username': fields.TextField(),
        # 'photo': fields.FileField(),  use this type if you have a file/image
    })

    city = fields.ObjectField(
        properties={
            'name': KeywordField(
                fields={
                    'raw': KeywordField(),
                    'suggest': fields.CompletionField(),
                }
            ),
            'covid_info': KeywordField(),
            'location': fields.GeoPointField(attr='location_field_indexing'),
            'country': fields.ObjectField(
                properties={
                    'name': KeywordField(
                        fields={
                            'raw': KeywordField(),
                            'suggest': fields.CompletionField(),
                        }
                    ),
                    'covid_info': KeywordField(),
                    'location': fields.GeoPointField(
                        attr='location_field_indexing'
                    )
                }
            )
        }
    )

     # Country object
    country = fields.NestedField(
        attr='country_indexing',
        properties={
            'name': StringField(
                fields={
                    'raw': KeywordField(),
                    'suggest': fields.CompletionField(),
                }
            ),
            'city': fields.ObjectField(
                properties={
                    'name': StringField(
                        fields={
                            'raw': KeywordField(),
                        },
                    ),
                },
            ),
        },
    )   


    created_at = fields.DateField(attr='created_at')

    has_covid = fields.BooleanField(attr='has_covid')

    class Django(object):
        model = CovidUser  # The model associate with this Document


    def get_queryset(self):
        """Not mandatory but to improve performance we can select related in one sql request"""
        return super(CovidUserDocument, self).get_queryset().select_related(
            'user'
        )

