from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST


#home page view function 
def home_view(request):
    return render(request, 'members/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a 'home' view or wherever you like
    else:
        form = SignUpForm()
    return render(request, 'members/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a 'home' view or wherever you like
    else:
        form = AuthenticationForm()
    return render(request, 'members/login.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Equipment, EquipmentQueue
from django.contrib import messages

@login_required
@require_POST
def join_queue(request, equipment_id):
    equipment = get_object_or_404(Equipment, id=equipment_id)
    # Check if the user is already in the queue
    if EquipmentQueue.objects.filter(user=request.user, equipment=equipment).exists():
        messages.error(request, 'You are already in the queue.')
    else:
        EquipmentQueue.objects.create(user=request.user, equipment=equipment)
        messages.success(request, 'You have joined the queue.')
    return redirect('equipment-detail', equipment_id=equipment_id)


@login_required
def view_queue(request, equipment_id):
    equipment = get_object_or_404(Equipment, id=equipment_id)
    queue = EquipmentQueue.objects.filter(equipment=equipment).select_related('user')
    context = {
        'equipment': equipment,
        'queue': queue
    }
    return render(request, 'members/equipment_queue.html', context)

from django.shortcuts import render
from .models import Equipment

def list_equipment(request):
    equipment_list = Equipment.objects.all()
    return render(request, 'members/list_equipment.html', {'equipment_list': equipment_list})

from django.shortcuts import get_object_or_404, render
from .models import Equipment, EquipmentQueue

def equipment_detail(request, equipment_id):
    equipment = get_object_or_404(Equipment, id=equipment_id)
    queue = EquipmentQueue.objects.filter(equipment=equipment).order_by('join_time')
    in_queue = queue.filter(user=request.user).exists()
    context = {
        'equipment': equipment,
        'queue': queue,
        'in_queue': in_queue,
        'queue_count': queue.count(),
        'user_position': None  # Initialize with None
    }
    if in_queue:
        user_queue_entry = EquipmentQueue.objects.get(user=request.user, equipment=equipment)
        user_position = EquipmentQueue.objects.filter(equipment=equipment, join_time__lt=user_queue_entry.join_time).count() + 1
        context['user_position'] = user_position

    return render(request, 'members/equipment_detail.html', context)

