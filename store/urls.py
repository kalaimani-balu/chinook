from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'playlists', views.PlayListViewSet)
router.register(r'media-types', views.MediaTypeViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'artists', views.ArtistViewSet)
router.register(r'albums', views.AlbumViewSet)
router.register(r'tracks', views.TrackViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'invoices', views.InvoiceViewSet)
router.register(r'invoice-items', views.InvoiceItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
