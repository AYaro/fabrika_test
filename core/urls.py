from django.conf.urls import include, url
from .views import AppViewSet
from rest_framework import routers

app_name = 'core'

router = routers.SimpleRouter()
router.register(r'apps', AppViewSet)

urlpatterns = [
    url(r'^core/', include((router.urls, app_name), namespace='core'))
]