from django.urls import path

from students import views

urlpatterns = [
    path('', views.get_all, name='index'),

]
