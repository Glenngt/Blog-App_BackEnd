import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def addPost(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({"Status":"Post Added Successfully"}))
    
@csrf_exempt
def deletePost(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({"Status":"Post Deleted Successfully"}))
    
@csrf_exempt
def searchPost(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({"Status":"Post Searching"}))
    
@csrf_exempt
def viewPost(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({"Status":"Viewing Post"}))