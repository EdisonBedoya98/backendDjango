from django.conf.urls import url, include
from django.urls import path
from . import views
from machinlearningmodel.views import index

urlpatterns = [
    url('api/index/', index),
    path('api/classifier/', views.ClasiffierListCreate.as_view()),
]
