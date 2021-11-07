from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return JsonResponse({"Nadal": "hard"})

def show_surface(request, surface_slug):
    return JsonResponse({"surface": surface_slug, "players": [{"name": "Nadal"}, {"name": "Sinner"}]})

def show_surface_player(request, surface_slug, player_name_slug):
    return JsonResponse({"surface": surface_slug, "player": [{"name": player_name_slug}]})

def my_view(request):
    host = request.META['HTTP_HOST']
    print(host)  # Eg. "foo.com"
    return HttpResponse(f"Got host {host}")
