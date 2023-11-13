from django.urls import path

from . import views

app_name = "characters"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:user_id>/character/", views.character, name="character"),
]