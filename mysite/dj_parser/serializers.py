from rest_framework import serializers
from dj_parser.models import Page, Link

class PageSerializer(serializers.HyperlinkedModelSerializer):
    links = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='link-detail')
    #?

    class Meta:
        model = Page
        fields = (
            'pk',
            'page_url',       
            'h1_count',
            'h2_count',
            'h3_count'
            )


class LinkSerializer(serializers.HyperlinkedModelSerializer):

    page = serializers.SlugRelatedField(queryset=Page.objects.all())

    class Meta:
        model = Link
        fields = ( 'a_url', )