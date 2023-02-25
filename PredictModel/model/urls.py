from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('PredictDigit', views.PredictDigit, name='PredictDigit'),
    path('get_csrf',views.get_csrf, name="get_csrf")
]