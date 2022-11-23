from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('homepage.urls'), name='homepage'),
    path('admin/', admin.site.urls, name='admin'),
    path('grappelli/', include('grappelli.urls'), name='grappelli'),
]
