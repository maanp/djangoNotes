from django.shortcuts import render , redirect
from .models import Notes
from datetime import datetime

# Create your views here.
def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')

        note = Notes(title=title,desc=desc,time=datetime.today())
        note.save()
        return redirect("/")
    else:
        notes = Notes.objects.all()
        param = {"notes":notes}
        return render(request, 'index.html',param)

def delete(request,nid):
    if request.method == "GET":
        # id = nid
        instance = Notes.objects.get(id=nid)
        instance.delete()
        return redirect('/')

    return redirect('/')

