
from django.urls import path
from . import views

urlpatterns = [

    path('',views.demo,name="demo"),
    # path('result/',views.result,name="result")
]
