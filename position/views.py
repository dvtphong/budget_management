from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Position
from .forms import PositionForm

@login_required
def position_list(request):
    positions = Position.objects.all().order_by('order_number')
    return render(request, 'position/position_list.html', {'positions': positions})

@login_required
def position_detail(request, pk):
    position = get_object_or_404(Position, pk=pk)
    return render(request, 'position/position_detail.html', {'position': position})

@login_required
def position_create(request):
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            position = form.save(commit=False)
            position.created_by = request.user
            position.save()
            messages.success(request, 'Position created successfully.')
            return redirect('position:list')
    else:
        form = PositionForm()
    return render(request, 'position/position_form.html', {'form': form, 'title': 'Create Position'})

@login_required
def position_update(request, pk):
    position = get_object_or_404(Position, pk=pk)
    if request.method == 'POST':
        form = PositionForm(request.POST, instance=position)
        if form.is_valid():
            position = form.save(commit=False)
            position.updated_by = request.user
            position.save()
            messages.success(request, 'Position updated successfully.')
            return redirect('position:list')
    else:
        form = PositionForm(instance=position)
    return render(request, 'position/position_form.html', {'form': form, 'title': 'Update Position'})

@login_required
def position_delete(request, pk):
    position = get_object_or_404(Position, pk=pk)
    if request.method == 'POST':
        position.delete()
        messages.success(request, 'Position deleted successfully.')
        return redirect('position:list')
    return render(request, 'position/position_confirm_delete.html', {'position': position})
