from django.shortcuts import render, redirect
import uuid
from .models import Application


def home (request) : 
    
    app = Application.objects.first()
    
    return render(request,'index.html',{'app':app})



def download (request) :

    app = Application.objects.first()
    
    response = redirect(f'media{app.file.url}')
    
    if 'User' in request.COOKIES :
        pass
    else :
        response.set_cookie('User',str(uuid.uuid4()))
        app.downloads = app.downloads + 1
        app.save()


    return response