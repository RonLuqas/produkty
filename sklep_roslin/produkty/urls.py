# produkty/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Strona główna
    path('produkt/<int:pk>/', views.produkt_detail, name='produkt_detail'),  # Strona szczegółowa produktu
]
