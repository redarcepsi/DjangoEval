from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
        return redirect('index')
    
    else : 
        return render(request,'connexion.html')

def index(request):
    all_event = Event.objects.all()
    return render(request,'index.html',{'Events':all_event})

def detail(request,event_id):
    event = Event.objects.get(pk = event_id)
    return render(request,'detail.html',{'event':event})

@login_required
def inscription(request,event_id):
    event = get_object_or_404(Event,id=event_id)
    event.participants.add(request.user)
    return redirect(index)