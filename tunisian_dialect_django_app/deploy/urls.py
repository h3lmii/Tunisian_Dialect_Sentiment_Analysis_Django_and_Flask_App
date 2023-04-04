from django.urls import path,include
from .views import index,result
urlpatterns = [
    path('',index, name="index"),
    path('result',result,name="result"),
]