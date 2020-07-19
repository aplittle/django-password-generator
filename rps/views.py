from django.shortcuts import render

def rps(request):
  return render(request, 'rps/rps.html')
