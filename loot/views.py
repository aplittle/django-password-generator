from django.shortcuts import render

def loot_home(request):
  return render(request, '/loot/home.html')
