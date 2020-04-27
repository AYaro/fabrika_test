
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
 

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^api/', include('core.urls', namespace='core')),
]
