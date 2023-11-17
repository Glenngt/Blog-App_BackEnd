import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def addUser(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({"Status" : "User Added Successfully"}))
    
@csrf_exempt
def deleteUser(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({"Status" : "User Deleted Successfully"}))
    
@csrf_exempt
def searchUser(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({"Status" : "Searching User"}))
    
@csrf_exempt
def viewUser(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({"Status" : "Viewing User"}))
    

