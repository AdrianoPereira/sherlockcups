from django.urls import path
from . import views


urlpatterns = [
    path('', views.carrefour_search, name='carrefour_search'),
    path('list_carrefour', views.list_carrefour, name='carrefour_list'),
]