from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.code import topNerController, topKeywordController, topPersonController, userKeywordController, userKeywordAssociationController, userKeywordSentimentController, newsRcmdBertController, sentimentBertController

@csrf_exempt
def topNer(request, type):
    if request.method == 'POST':
        if type == 'api_get_ner_topword':
            return topNerController.api_get_ner_topword(request)
@csrf_exempt
def topKeyword(request, type):
    if request.method == 'POST':
        if type == 'api_get_cate_topword':
            return topKeywordController.api_get_cate_topword(request)
@csrf_exempt
def topPerson(request, type):
    if request.method == 'POST':
        if type == 'api_get_topPerson':
            return topPersonController.api_get_topPerson(request)
@csrf_exempt
def userKeyword(request, type):
    if request.method == 'POST':
        if type == 'api_get_top_userkey':
            return userKeywordController.api_get_top_userkey(request)
@csrf_exempt
def userKeywordAssociation(request, type):
    if request.method == 'POST':
        if type == 'api_get_userkey_associate':
            return userKeywordAssociationController.api_get_userkey_associate(request)
@csrf_exempt
def userKeywordSentiment(request, type):
    if request.method == 'POST':
        if type == 'api_get_userkey_sentiment':
            return userKeywordSentimentController.api_get_userkey_sentiment(request)
@csrf_exempt
def newsRcmdBert(request, type):
    if request.method == 'POST':
        if type == 'api_query_keyword_cate_news':
            return newsRcmdBertController.api_query_keyword_cate_news(request)
        if type == 'api_news_content':
            return newsRcmdBertController.api_news_content(request)
@csrf_exempt
def sentimentBert(request, type):
    if request.method == 'POST':
        if type == 'api_get_sentiment':
            return sentimentBertController.api_get_sentiment(request)