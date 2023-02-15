from django.shortcuts import render
from django.http import HttpResponse
from . models import Place
from . models import Team

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    te=Team.objects.all()
    return render(request,"index.html",{'result':obj,'team':te})

# def result(request):
#
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     s = x+y
#     d = x-y
#     p = x*y
#     q = x/y
#     return render(request,'result.html',{'sum':s,'dif':d,'pro':p,'quo':q})
