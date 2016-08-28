from django import views
from django.http import HttpResponse
from django.shortcuts import render_to_response, render

from Minerals.models import Mineral


def mineral_list(request):
    all_minerals = Mineral.objects.all().order_by('name')

    return render(request, 'index.html', {'all_minerals': all_minerals})

def mineral_detail(request, id):
    try:
        mineral = Mineral.objects.get(id=id)
    except Mineral.DoesNotExist:
        mineral = None

    return render(request, 'detail.html', {'mineral': mineral})
