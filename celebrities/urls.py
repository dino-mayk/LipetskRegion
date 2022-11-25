from django.urls import path, re_path

from celebrities import views

app_name = 'celebrities'

urlpatterns = [
    path('', views.list, name='list'),
    re_path(r'(?P<pk>^[1-9]\d*)/$', views.detail, name='detail'),
]
