from django.urls import path, re_path

from landmarks import views

app_name = 'landmarks'

urlpatterns = [
    path('', views.list, name='list'),
    re_path(r'(?P<pk>^[1-9]\d*)/$', views.detail, name='detail'),
]
