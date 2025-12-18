from django.shortcuts import render

def fishington_home(request):
  return render(request, "website/fishington.html")

def crewLive(request):
  return render(request, "website/crewLive.html")
