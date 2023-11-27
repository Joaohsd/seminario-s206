"""
URL configuration for swagger project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from cars.views import CarViewSet, ParkingLotViewSet


router = routers.DefaultRouter()
router.register(r"cars", CarViewSet, basename="cars")
router.register(r"parking-lots", ParkingLotViewSet, basename="parking-lots")


# Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Cars API",
      default_version='v1',
      description="Cars CRUD",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@support.com"),
      license=openapi.License(name="INATEL License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

api_info = openapi.Info(title="Snippets API", default_version="v1", description="Project description",)


urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]
