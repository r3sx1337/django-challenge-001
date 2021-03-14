from rest_framework import serializers
from authors.api.serializers import AuthorSerializer
from articles.models import Article
from news import settings

class ArticleSerializer(serializers.ModelSerializer):

    author = AuthorSerializer()

    class Meta:
        model = Article
        exclude=('created_at','updated_at')
        depth = 1

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        request = self.context.get('request')
        if request.auth is None:
            fields.pop('body', None)
        return fields