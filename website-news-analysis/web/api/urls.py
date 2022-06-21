from django.urls import path
from . import views

app_name="api"

urlpatterns = [
    path('ner/<type>', views.ner),
    path('keyword/<type>', views.keyword),
    path('person/<type>', views.person),
]
