from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
import glob,os
from .models import files
from .forms import fileform,check_box
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_protect


@login_required
def media(request):
    usr=request.user #currently logged user id(name)
    
    #**********************************************************************************************
    #display files in folder/diretory
    mp4_files = map(os.path.basename, glob.glob('media/**/*.mp4', recursive=True)+glob.glob('media/**/*.mkv', recursive=True))   
    #**********************************************************************************************
    context = {
        "usr":usr,
        "mp4_files":mp4_files,
    }
    
    return render(request, "registration/media.html", context,)

@login_required
def media_handling(request,video):
    video_url = settings.MEDIA_URL+video
    vid = map(os.path.basename, glob.glob('media/**/*.mp4', recursive=True)+glob.glob('media/**/*.mkv', recursive=True)) 
    vid1 = ['/media/' + s for s in vid]
    context = {
        "vid1":vid1,
        "vid":vid,
        "video":video,
        "video_url":video_url,
    }
    
    return render(request,"registration/video_stream.html",context)

def homepage(request):
    usr=request.user
    context={
        'user':usr,
    }
    return render(request,"registration/homepage.html")

def about(request):
    return render(request,"registration/about.html")

@csrf_protect
def upload(request):
    message = 'Upload as many files as you want!'
    # Load documents for the list page
    documents = files.objects.all()
    # Handle file upload
    if request.method == 'POST':
        form = fileform(request.POST, request.FILES)
        if form.is_valid():
            newdoc = files(file_up=request.FILES['file_up'])
            newdoc.save()

            # Redirect to the document list after POST
            return redirect('upload')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = fileform()  # An empty, unbound form
    
    # Render list page with the documents and the form
    context = {
        'documents': documents, 'form': form, 'message': message
        }
    return render(request, 'registration/upload.html', context)



def deleted(request):
    documents = files.objects.all()
    delete1 = map(os.path.basename, glob.glob('media/**/*.mp4', recursive=True)+glob.glob('media/**/*.mkv', recursive=True))
    
       
    return HttpResponse('deleted')