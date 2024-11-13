from django.shortcuts import render, redirect, get_object_or_404
from .forms import ChildForm
from .models import Child
from datetime import date
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_child(request):
    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('children:child_list')
    else:
        form = ChildForm()
    return render(request, 'children/add_child.html', {'form': form})

@login_required
def edit_child(request, pk):
    child = get_object_or_404(Child, pk=pk)
    if request.method  == 'POST':
        form = ChildForm(request.POST, instance=child)
        if form.is_valid():
            form.save()
            return redirect('children:child_list')

    else:
        form = ChildForm(instance=child)

    return render(request, 'children/edit_child.html', {'form': form, 'child': child})

@login_required
def delete_child(request, pk):
    child = get_object_or_404(Child, pk=pk)
    if request.method == 'POST':
        child.delete()
        return redirect('children:child_list')
    return render(request, 'children/delete_child.html', {'child': child})

@login_required
def child_list(request):
    children = Child.objects.all()
    for child in children:
        if child.date_of_birth:
            today = date.today()
            age = today.year - child.date_of_birth.year
            if (today.month, today.day) < (child.date_of_birth.month, child.date_of_birth.day):
                age -= 1
            child.age = age

    context = {
        'children': children,
    }
    return render(request, 'children/child_list.html', context)
