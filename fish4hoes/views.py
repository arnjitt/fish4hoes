from django.shortcuts import render, redirect
from .models import Friend
from .forms import FriendForm, FriendEnergyFormSet

def fishington_home(request):
  return render(request, "website/fishington.html")

def crewLive(request):
  return render(request, "website/crewLive.html")

def projectsPage(request):
  return render(request, "website/projects.html")

def chat_room(request):
  friends = Friend.objects.all()
  # sample messages // not from DB
  messages = [
    {"author": "System", "text": "Welcome to 4x4 demo"},
    {"author": "Cass", "text": "I love Overwatch!!!"},
    {"author": "Bryan", "text": "Ohhhhhahhhahhhahhhah"},
    {"author": "Mikey", "text": "Toughness"},
  ]
  return render(request, "website/chat_room.html", {"friends": friends, "messages": messages})


## Page Logic held for adding Friends to database
def add_friend(request):
  qs = Friend.objects.all()

  if request.method == "POST":
    friend_form = FriendForm(request.POST, prefix="new")
    formset = FriendEnergyFormSet(
      request.POST, 
      queryset=qs, 
      prefix="energy"
    )

    if "save_new" in request.POST and friend_form.is_valid():
      friend_form.save()
      return redirect("add_friend")
    
    if "save_energy" in request.POST and formset.is_valid():
      formset.save()
      return redirect("add_friend")
  else:
      friend_form = FriendForm(prefix="new")
      formset = FriendEnergyFormSet(queryset=qs, prefix="energy")

  return render(request, "website/add_friend.html", {
    "friend_form": friend_form,
    "formset": formset,
  })