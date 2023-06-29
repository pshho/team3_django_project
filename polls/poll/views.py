from django.shortcuts import render, redirect
from map.models import SeouljRent, SeoulReal
from django.forms.models import model_to_dict
from django.http import JsonResponse


def index(request):
    return render(request, 'poll/index.html')

def index2(request):
    return redirect('poll/')

def index_search(request):
    if request.method == 'GET':
        query = request.GET.get('search_data')

        context = {
            'query': query,
        }

        return JsonResponse(context)
    return render(request, 'poll/index.html')

# 서울 부동산 정보 데이터베이스 파싱
def index_search_list(request):
    if request.method == 'GET':
        seoul_rent = SeouljRent.objects.all()
        seoul_real = SeoulReal.objects.all()
        jrent = [model_to_dict(seoul) for seoul in seoul_rent]
        real = [model_to_dict(seoul) for seoul in seoul_real]

        results = {
            'jrent': jrent,
            'real': real
        }
        return JsonResponse(results, safe=False)

    return JsonResponse({'result': '실패'})