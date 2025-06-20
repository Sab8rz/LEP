from django.urls import path
from . import views
from .api.views import LepCalculateAPI, WireAPI, LepCalculateManualAPI, SubjectAPI

urlpatterns = [
    path('', views.index, name='lep_calculate'),

    # API
    path('api/subjects/', SubjectAPI.as_view()),
    path('api/wires/', WireAPI.as_view()),
    path('api/lep-calculate/', LepCalculateAPI.as_view()),
    path('api/lep-calculate-manual/', LepCalculateManualAPI.as_view())
]