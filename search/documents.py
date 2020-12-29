from django.contrib.auth import get_user_model
from django_elasticsearch_dsl import Document, fields, Index
from django_elasticsearch_dsl.registries import registry
from .models import CovidUser
from elasticsearch_dsl import analyzer

User = get_user_model()


SEARCH_INDEX = Index('search')

SEARCH_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)


#@registry.register_document
@SEARCH_INDEX.doc_type
class CovidUserDocument(Document):
    id = fields.IntegerField(attr='id')

    user = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'username': fields.TextField(),
        # 'photo': fields.FileField(),  use this type if you have a file/image
    })

    city = fields.TextField(
        fields={
            'raw': fields.KeywordField(),
            'suggest': fields.CompletionField(),
        }
    )

    address = fields.TextField(
        fields={
            'raw': fields.KeywordField(),
            'suggest': fields.CompletionField(),
        }
    )

    state_province = fields.TextField(
        fields={
            'raw': fields.KeywordField(),
        }
    )
    country = fields.TextField(
        fields={
            'raw': fields.KeywordField(),
            'suggest': fields.CompletionField(),
        }
    )
    
    # Location
    location = fields.GeoPointField(attr='location_field_indexing')

    created_at = fields.DateField(attr='created_at')

    has_covid = fields.BooleanField(attr='has_covid')

    class Django(object):
        model = CovidUser  # The model associate with this Document


    def get_queryset(self):
        """Not mandatory but to improve performance we can select related in one sql request"""
        return super(CovidUserDocument, self).get_queryset().select_related(
            'user'
        )

    # def get_instances_from_related(self, related_instance):
    #     """If related_models is set, define how to retrieve the instance(s) from the related model.
    #     The related_models option should be used with caution because it can lead in the index
    #     to the updating of a lot of items.
    #     """
    #     if isinstance(related_instance, User):
    #         return related_instance.CovidUser.all()

