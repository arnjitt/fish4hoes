from django.shortcuts import render

def fishington_home(request):
  return render(request, "/fishington.html")
