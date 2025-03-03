from django.urls import path, include
from api.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/', include('api.urls')),
]
