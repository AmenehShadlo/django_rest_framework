
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_app/', include("api_app.urls")),
    path('testapp/', include("testapp.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
