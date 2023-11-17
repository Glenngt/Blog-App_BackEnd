import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from register.serializer import RegisterSerializer
from register.models import RegisterModel
from django.db.models import Q

# Create your views here.
@csrf_exempt
def addUser(request):
    if request.method == "POST":
        recieved_data = json.loads(request.body)
        print(recieved_data)
        serializer_check = RegisterSerializer(data=recieved_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"Status" : "User Added Successfully"}))
        else:
            return HttpResponse(json.dumps({"Status" : "User Add Failed"}))

    
@csrf_exempt
def deleteUser(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({"Status" : "User Deleted Successfully"}))
    
@csrf_exempt
def searchUser(request):
    if request.method == "POST":
        recieved_data = json.loads(request.body)
        print(recieved_data)
        getName = recieved_data["name"]
        data = list(RegisterModel.objects.filter(Q(name__iscontains=getName)).values())
        return HttpResponse(json.dumps(data))
    
@csrf_exempt
def viewUser(request):
    if request.method == "POST":
        userList = RegisterModel.objects.all()
        serialized_data = RegisterSerializer(userList,many=True)
        return HttpResponse(json.dumps(serialized_data.data))
    

