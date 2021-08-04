from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Service


@registry.register_document
class ServiceDocument(Document):
    class Index:
        #имя эластик индекса
        name = 'service'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Service
        fields = [
            'category',
            'description',
        ]

def search(query_string):
    company = ServiceDocument.search().filter("term", description=query_string)
    return company