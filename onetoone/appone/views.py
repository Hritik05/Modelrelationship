from django.shortcuts import render
from django.http import HttpResponse
from appone.models import Place,Restaurant,Waiter,Reporter,Article,Publication,Articles

# Create your views here.
def index(request):
    my_dict = {'insert_me':"Hello I am appone/index.html"}
    return render(request,'appone/index.html',context=my_dict)














