import urllib
import json

from django.http import JsonResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'poll/index.html')

def index_search(request):
    if request.method == 'GET':
        query = request.GET.get('search_data')

        context = {
            'query': query,
        }

        return JsonResponse(context)
    return render(request, 'poll/index.html')