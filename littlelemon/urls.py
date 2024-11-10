from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #apps
    path('api/',include('littlelemonAPI.urls')),
    # Djoser 
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.authtoken')),
]
