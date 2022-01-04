from django.shortcuts import render , redirect
from .models import Notes
from datetime import datetime

# Create your views here.
def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        pic = request.POST.get('pic')

        note = Notes(title=title,desc=desc,img=pic,time=datetime.today())
        note.save()
        return redirect("/")
    else:
        notes = Notes.objects.all()
        param = {"notes":notes}
        return render(request, 'index.html',param)

def delete(request,id):
    if request.method == "GET":
        # id = nid
        instance = Notes.objects.get(id=id)
        instance.delete()
        return redirect('/')

    return redirect('/')

