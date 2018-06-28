from rest_framework import serializers
from dj_parser.models import Page, Link

class PageSerializer(serializers.HyperlinkedModelSerializer):
    urls = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='url')
    #?

    class Meta:
        model = Page
        fields = (  
            'pk',   
            'page_url',
            'h1',
            'h2',
            'h3',
            'a',
            'urls',
            )


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    #page = serializers.SlugRelatedField(queryset=Page.objects.all())

    class Meta:
        model = Link
        fields = ( 'url', )