import graphene

from graphene_django.types import DjangoObjectType

from . import models


class PlayListType(DjangoObjectType):
    class Meta:
        model = models.PlayList


class MediaTypeType(DjangoObjectType):
    class Meta:
        model = models.MediaType


class Query(object):
    all_playlists = graphene.List(PlayListType)
    all_media_types = graphene.List(MediaTypeType)

    def resolve_all_playlists(self, info, **kwargs):
        return models.PlayList.objects.all()

    def resolve_all_media_types(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return models.MediaType.objects.all()
