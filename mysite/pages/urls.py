# pages/urls.py
from django.urls import path
from . import views
app_name = 'pages'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('favorite/<str:name>', views.favorite, name='favorite'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('buy/', views.buy, name='buy'),
    path('lotto/', views.lotto, name='lotto'),
    path('artii/', views.artii, name='artii'),
    path('result/', views.result, name='result'),
]