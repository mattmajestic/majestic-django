from django.urls import path
from okta import views

urlpatterns = [
    path('', views.okta, name='okta'),
]