from django.db import models


class PlayList(models.Model):
    id = models.AutoField(primary_key=True, db_column='PlaylistId')
    name = models.CharField(max_length=200)
    # tracks = models.ManyToManyField('Track', through='PlayListTrack')

    class Meta:
        db_table = 'playlists'


class MediaType(models.Model):
    id = models.AutoField(primary_key=True, db_column='MediaTypeId')
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'media_types'


class Genre(models.Model):
    id = models.AutoField(primary_key=True, db_column='GenreId')
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'genres'


class Artist(models.Model):
    id = models.AutoField(primary_key=True, db_column='ArtistId')
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'artists'


class Album(models.Model):
    id = models.AutoField(primary_key=True, db_column='AlbumId')
    title = models.CharField(max_length=200)
    artist_id = models.ForeignKey(Artist, on_delete=models.DO_NOTHING, db_column='ArtistId')

    class Meta:
        db_table = 'albums'


class Track(models.Model):
    id = models.AutoField(primary_key=True, db_column='TrackId')
    album_id = models.ForeignKey(Album, db_column='AlbumId', on_delete=models.DO_NOTHING)
    media_type_id = models.ForeignKey(MediaType, db_column='MediaTypeId', on_delete=models.DO_NOTHING)
    genre_id = models.ForeignKey(Genre, db_column='GenreId', on_delete=models.DO_NOTHING)
    composer = models.CharField(max_length=200)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, db_column='UnitPrice')

    class Meta:
        db_table = 'tracks'


class PlayListTrack(models.Model):
    play_list_id = models.ForeignKey(PlayList, on_delete=models.DO_NOTHING, db_column='PlayListId')
    track_id = models.ForeignKey(Track, on_delete=models.DO_NOTHING, db_column='TrackId')

    class Meta:
        db_table = 'playlist_track'


class Employee(models.Model):
    id = models.AutoField(primary_key=True, db_column='EmployeeId')
    last_name = models.CharField(max_length=200, db_column='LastName')
    first_name = models.CharField(max_length=200, db_column='FirstName')
    title = models.CharField(max_length=200)
    reports_to = models.ForeignKey('self', db_column='ReportsTo', on_delete=models.DO_NOTHING)
    birth_date = models.DateTimeField(db_column='BirthDate')
    hire_date = models.DateTimeField(db_column='HireDate')
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200, db_column='PostalCode')
    phone = models.CharField(max_length=200)
    fax = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    class Meta:
        db_table = 'employees'


class Customer(models.Model):
    id = models.AutoField(primary_key=True, db_column='CustomerId')
    last_name = models.CharField(max_length=200, db_column='LastName')
    first_name = models.CharField(max_length=200, db_column='FirstName')
    company = models.CharField(max_length=200)
    support_rep_id = models.ForeignKey(Employee, db_column='SupportRepId', on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200, db_column='PostalCode')
    phone = models.CharField(max_length=200)
    fax = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    class Meta:
        db_table = 'customers'


class Invoice(models.Model):
    id = models.AutoField(primary_key=True, db_column='InvoiceId')
    customer_id = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, db_column='CustomerId')
    invoice_date = models.DateTimeField(db_column='InvoiceDate')
    billing_address = models.CharField(max_length=200, db_column='BillingAddress')
    billing_city = models.CharField(max_length=200, db_column='BillingCity')
    billing_state = models.CharField(max_length=200, db_column='BillingState')
    billing_country = models.CharField(max_length=200, db_column='BillingCountry')
    billing_postal_code = models.CharField(max_length=200, db_column='BillingPostalCode')
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'invoices'


class InvoiceItem(models.Model):
    id = models.AutoField(primary_key=True, db_column='InvoiceLineId')
    invoice_id = models.ForeignKey(Invoice, on_delete=models.DO_NOTHING, db_column='InvoiceId')
    track_id = models.ForeignKey(Track, on_delete=models.DO_NOTHING, db_column='TrackId')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, db_column='UnitPrice')
    quantity = models.IntegerField()

    class Meta:
        db_table = 'invoice_items'
