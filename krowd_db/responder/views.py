from django.shortcuts import render
from django.http import HttpResponse,FileResponse
# Create your views here.

def return_img(request):
    img=open('media','rb')
    response=FileResponse(img)
    return response

