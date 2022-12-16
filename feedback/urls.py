from django.urls import path

from feedback import views

app_name = 'feedback'

urlpatterns = [
    path('', views.feedback, name='feedback'),
    path('feedback_thank_you/', views.feedback_thank_you, name='feedback_thank_you'),
]
