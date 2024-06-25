from django.shortcuts import render,redirect
from .models import Note
from django.contrib import messages
# Create your views here.
def index(request):
    notes = Note.objects.all()
    if request.method == 'POST':
        task = request.POST.get('task')
        task_data = Note.objects.create(task=task)
        task_data.save()
        return redirect('index')
    return render(request,'index.html',{'notes':notes})

def update_note(request,id):
    note=Note.objects.get(id = id)
    if request.method == 'POST':
        note.task = request.POST.get('task')
        note.save()
        messages.success(request,'Successfully Edited')
        return redirect('index')
    return render(request,'edit.html',{'note':note})

def delete_note(request,id):
    note = Note.objects.get(id = id)
    note.delete()
    messages.success(request,'Successfully Deleted')
    return redirect('index')
