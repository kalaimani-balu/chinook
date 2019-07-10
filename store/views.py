from rest_framework import viewsets

from . import serializers, models


class PlayListViewSet(viewsets.ModelViewSet):
    queryset = models.PlayList.objects.all()
    serializer_class = serializers.PlayListSerializer


class MediaTypeViewSet(viewsets.ModelViewSet):
    queryset = models.MediaType.objects.all()
    serializer_class = serializers.MediaTypeSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = models.Artist.objects.all()
    serializer_class = serializers.ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = models.Album.objects.all()
    serializer_class = serializers.AlbumSerializer


class TrackViewSet(viewsets.ModelViewSet):
    queryset = models.Track.objects.all()
    serializer_class = serializers.TrackSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = models.Invoice.objects.all()
    serializer_class = serializers.InvoiceSerializer


class InvoiceItemViewSet(viewsets.ModelViewSet):
    queryset = models.InvoiceItem.objects.all()
    serializer_class = serializers.InvoiceItemSerializer
