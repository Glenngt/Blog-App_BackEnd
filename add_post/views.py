import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from add_post.serializer import PostSerializer
from add_post.models import AddPostModel
from django.db.models import Q

# Create your views here.
@csrf_exempt
def addPost(request):
    if request.method == "POST":
        recieved_data = json.loads(request.body)
        print(recieved_data)
        serializer_check = PostSerializer(data=recieved_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"Status":"Post Added Successfully"}))
        else:
            return HttpResponse(json.dumps({"Status":"Post Adding Failed"}))
    
@csrf_exempt
def deletePost(request):
    if request.method == "POST":
        return HttpResponse(json.dumps({"Status":"Post Deleted Successfully"}))
    
@csrf_exempt
def searchPost(request):
    if request.method == "POST":
        recieved_data = json.loads(request.body)
        print(recieved_data)
        getTitle = recieved_data["title"]
        data = list(AddPostModel.objects.filter(Q(title__iscontains=getTitle)).values())
        return HttpResponse(json.dumps(data))
    
@csrf_exempt
def viewPost(request):
    if request.method == "POST":
        postList = AddPostModel.objects.all()
        seralized_data = PostSerializer(postList,many=True)
        return HttpResponse(json.dumps(seralized_data.data))
    

@csrf_exempt
def viewAllPost(request):
    if request.method == "POST":
        postList = AddPostModel.objects.filter(userid=request.userid)
        seralized_data = PostSerializer(postList,many=True)
        return HttpResponse(json.dumps(seralized_data.data, safe = False))