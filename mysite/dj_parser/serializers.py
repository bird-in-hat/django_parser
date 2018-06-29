from rest_framework import serializers
from dj_parser.models import Page, Link

import urllib

class PageSerializer(serializers.HyperlinkedModelSerializer):
    urls = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='url',
        )
    page_url = serializers.URLField(
        max_length=400,
        write_only=True
        )

    def validate_page_url(self, page_url):
        try:
            urllib.request.urlopen(page_url)
        except urllib.error.URLError:
            raise serializers.ValidationError('DNS address could not be found')
        return page_url

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
        read_only_fields = (  
            'h1',
            'h2',
            'h3',
            'a',
            )


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    #page = serializers.SlugRelatedField(queryset=Page.objects.all())

    class Meta:
        model = Link
        fields = ( 'url', )