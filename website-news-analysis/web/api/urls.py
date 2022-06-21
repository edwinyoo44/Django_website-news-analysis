from django.urls import path
from . import views

app_name="api"

urlpatterns = [
    path('topNer/<type>', views.topNer),
    path('topKeyword/<type>', views.topKeyword),
    path('topPerson/<type>', views.topPerson),
    path('userKeyword/<type>', views.userKeyword),
    path('userKeywordAssociation/<type>', views.userKeywordAssociation),
    path('userKeywordSentiment/<type>', views.userKeywordSentiment),
    path('newsRcmdBert/<type>', views.newsRcmdBert),
    path('sentimentBert/<type>', views.sentimentBert),
]
