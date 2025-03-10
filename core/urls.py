from decouple import config, Csv
from django.urls import path, include
from api.views import IndexView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Django API",
      default_version='v1.0.0',
      description="A simple Django REST API",
      terms_of_service="https://www.example.com/terms/",
      contact=openapi.Contact(email="conn@ewoooba.io"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=[],
   validators=[],
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/', include('api.urls')),
    path('tasks/', include('tasks.urls')),
    
    # Swagger UI URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]