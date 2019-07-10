from rest_framework import serializers

from . import models


class PlayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlayList
        fields = ('id', 'name')

        # fields = ('id', 'name', 'tracks')


class MediaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MediaType
        fields = ('id', 'name')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = ('id', 'name')


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Artist
        fields = ('id', 'name')


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Album
        fields = ('id', 'title', 'artist_id')


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Track
        fields = ('id', 'album_id', 'media_type_id', 'genre_id', 'composer', 'milliseconds', 'bytes', 'unit_price')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ('id',
                  'last_name',
                  'first_name',
                  'title',
                  'reports_to',
                  'birth_date',
                  'hire_date',
                  'address',
                  'city',
                  'state',
                  'country',
                  'postal_code',
                  'phone',
                  'fax',
                  'email')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ('id',
                  'last_name',
                  'first_name',
                  'company',
                  'support_rep_id',
                  'address',
                  'city',
                  'state',
                  'country',
                  'postal_code',
                  'phone',
                  'fax',
                  'email')


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invoice
        fields = ('id',
                  'customer_id',
                  'invoice_date',
                  'billing_address',
                  'billing_city',
                  'billing_state',
                  'billing_country',
                  'billing_postal_code',
                  'total')


class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvoiceItem
        fields = ('id', 'invoice_id', 'track_id', 'unit_price', 'quantity')
