from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User

def index(request):
    all_users = User.objects.all()
    context = { "all_users": all_users }
    return render(request, "users/index.html", context)

def character(request, user_id):
    user = User.objects.get(pk=user_id)
    character = user.character_set.get() if user and user.character_set.exists() else None
    return render(request, "users/character.html", { "character": character, "user": user })