from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import redirect

def index(request):
    return redirect("/views/topKeyword/index")

@csrf_exempt
def topNer(request, type):
    if request.method == 'GET':
        if type == 'index':
            context = {'title': 'NER熱門分析'}
            return render(request, 'top_ner_index.html', context)
@csrf_exempt
def topKeyword(request, type):
    if request.method == 'GET':
        if type == 'index':
            context = {'title': '熱門關鍵詞分析'}
            return render(request, 'top_keyword_index.html', context)
@csrf_exempt
def topPerson(request, type):
    if request.method == 'GET':
        if type == 'index':
            context = {'title': '熱門人物排行分析'}
            return render(request, 'top_person_index.html', context)
@csrf_exempt
def userKeyword(request, type):
    if request.method == 'GET':
        if type == 'index':
            context = {'title': '你的關鍵詞熱門度分析'}
            return render(request, 'user_keyword_index.html', context)
@csrf_exempt
def userKeywordAssociation(request, type):
    if request.method == 'GET':
        if type == 'index':
            context = {'title': '全文檢索與關聯新聞分析'}
            return render(request, 'user_keyword_association_index.html', context)
@csrf_exempt
def userKeywordSentiment(request, type):
    if request.method == 'GET':
        if type == 'index':
            context = {'title': '你的關鍵詞情緒分析'}
            return render(request, 'user_keyword_sentiment_index.html', context)
@csrf_exempt
def newsRcmdBert(request, type):
    if request.method == 'GET':
        if type == 'index':
            context = {'title': '新聞瀏覽與推薦(Bert)'}
            return render(request, 'news_rcmd_bert_index.html', context)
@csrf_exempt
def sentimentBert(request, type):
    if request.method == 'GET':
        if type == 'index':
            context = {'title': '文章情緒判斷系統'}
            return render(request, 'sentiment_bert_index.html', context)
