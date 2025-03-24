from django.urls import path
from . import views


urlpatterns = [
    # path('', views.home),
    # path('lep/', views.index),
    path('', views.Index.as_view(), name='lep_calculate')
]