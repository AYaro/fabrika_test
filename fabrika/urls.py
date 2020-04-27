
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
import os
 
schema_view = get_schema_view(
    openapi.Info(
        title="Fabrika Test",
        default_version='v1',
        description="REST docs",
        contact=openapi.Contact(email="0370384@mail.ru"),
    ),
    url=os.environ.get('BASE_URL', 'http://localhost:8000/api'),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^api/', include('core.urls', namespace='core')),
    url(r'^api/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
