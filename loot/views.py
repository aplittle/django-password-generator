from django.shortcuts import render
from django.http import HttpRequest
from .models import Loot, Coin

def home(request):
  return render(request, 'loot/home.html')

def addloot(request):
  return render(request, 'loot/addloot.html')

def addnewloot(request):
  quant = request.POST.get('quantity')
  desc = request.POST.get('desc')
  estvalue = request.POST.get('est_value')
  cointype = request.POST.get('coin_type')
  calctype = request.POST.get('calc_type')
  notes = request.POST.get('notes')
  
  total = int(quant) * int(estvalue)
  
  context = {
    "Quant": quant,
    "Desc": desc,
    "EstValue": estvalue,
    "CoinType": cointype,
    "CalcType": calctype,
    "Total": total,
    "Notes": notes,
  }
  
  return render(request, 'loot/addnewloot.html', context)
