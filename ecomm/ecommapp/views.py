from django.shortcuts import render,HttpResponse
# Create your views here.
from django.views import View
def about():

    return HttpResponse("this is about page")   

def contact(request):

    return HttpResponse("hello from contact page")   

def home(request):

    return HttpResponse("hello from home page")   

def edit(request,rid):
    print("Id to be edited:",rid)

    return HttpResponse("Id to be edited:"+rid)   

def delete(request,rid):
    print("Id to be deleted:",rid)

    return HttpResponse("Id to be deleted:"+rid)   

class SimpleView(View):
    def get(self,request):
        return HttpResponse("Hello from simpleview")

    
def hello(req):
    contxt = {}
    contxt["name"] = "prasanth"
    contxt["x"] =654
    contxt["y"] =100
    contxt['l']=[10,20,30,40,50,60,70,80,90]
    contxt['products']=[
        {"id":1,"name": "samsung","cat":"mobile","price":25000},
        {"id":2,"name": "jeans","cat":"cloth","price":1500},
        {"id":3,"name": "nike","cat":"shoes","price":3000},
        {"id":4,"name": "apple","cat":"mobile","price":80000}
  
    ]
    return render(req,"hello.html",contxt)


