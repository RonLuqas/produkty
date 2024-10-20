# produkty/views.py
from django.shortcuts import render, get_object_or_404
from .models import Produkt, Tag
from datetime import datetime

def get_season():
    month = datetime.now().month
    if 3 <= month <= 5:
        return 'spring'
    elif 6 <= month <= 8:
        return 'summer'
    elif 9 <= month <= 11:
        return 'autumn'
    else:
        return 'winter'

def home(request):
    produkty = Produkt.objects.all()
    tagi = Tag.objects.all()
    min_cena = request.GET.get('min_cena')
    max_cena = request.GET.get('max_cena')
    selected_tagi = request.GET.getlist('tagi')
    
    if selected_tagi:
        produkty = produkty.filter(tagi__nazwa__in=selected_tagi).distinct()
    if min_cena:
        produkty = produkty.filter(cena__gte=min_cena)
    if max_cena:
        produkty = produkty.filter(cena__lte=max_cena)
    
    season = get_season()

    return render(request, 'produkty/home.html', {
        'produkty': produkty,
        'tagi': tagi,
        'season': season,
    })

def produkt_detail(request, pk):
    produkt = get_object_or_404(Produkt, pk=pk)
    return render(request, 'produkty/produkt_detail.html', {'produkt': produkt})