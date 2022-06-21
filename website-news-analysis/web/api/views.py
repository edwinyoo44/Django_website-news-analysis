from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.code import nerController, keywordController, personController


@csrf_exempt
def ner(request, type):
    if request.method == 'POST':
        if type == 'api_get_ner_topword':
            return nerController.api_get_ner_topword(request)
@csrf_exempt
def keyword(request, type):
    if request.method == 'POST':
        if type == 'api_get_cate_topword':
            return keywordController.api_get_cate_topword(request)
@csrf_exempt
def person(request, type):
    if request.method == 'POST':
        if type == 'api_get_topPerson':
            return personController.api_get_topPerson(request)
