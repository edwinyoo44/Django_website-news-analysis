from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import redirect

def index(request):
    return redirect("/views/keyword/index")

@csrf_exempt
def ner(request, type):
    if request.method == 'GET':
        if type == 'index':
            context = {'title': 'NER熱門分析'}
            return render(request, 'ner_index.html', context)
@csrf_exempt
def keyword(request, type):
    if request.method == 'GET':
        if type == 'index':
            context = {'title': '熱門關鍵詞分析'}
            return render(request, 'keyword_index.html', context)
@csrf_exempt
def person(request, type):
    if request.method == 'GET':
        if type == 'index':
            context = {'title': '熱門人物排行分析'}
            return render(request, 'person_index.html', context)
