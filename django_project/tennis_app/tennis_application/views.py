from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

from django.views.decorators.http import require_GET
from django.views.decorators.http import require_POST

@require_POST
def create_user(request):
    return JsonResponse({"id": 1})

@require_GET
def read_user(request, user_id):
    return JsonResponse({"id": user_id})

@require_GET
def hello(request):
    msg = "Welcome: tennis application"
    return HttpResponse(msg, content_type='text/plain')

@require_GET
def show_surface(request, surface_slug):
    if surface_slug == 'clay':   
        return JsonResponse({"surface": surface_slug, "players": [{"name": "Nadal"}, {"name": "Borg"}]})
    elif surface_slug == 'hard':
        return JsonResponse({"surface": surface_slug, "players": [{"name": "Djokovich"}, {"name": "Medvedev"}]})

@require_GET
def show_surface_player(request, surface_slug, player_name_slug):
    return JsonResponse({"surface": surface_slug, "player": [{"name": player_name_slug}]})

@require_GET
def get_my_ip(request):
    return JsonResponse({
        'ip': request.META.get('HTTP_X_REAL_IP') or request.META.get('REMOTE_ADDR'),
    })
