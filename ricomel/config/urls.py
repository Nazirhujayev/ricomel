"""
URL configuration for ricomel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
       title="Ricomel API",
       default_version="v1",
       description="Ricomel Admin API",
       terms_of_service="https://localhost:8000",
       contact=openapi.Contact(email="admin@bekzodbek.com"),
       license=openapi.License(name="License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
        )




urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("common.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0),name="schema-swagger-ui"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
