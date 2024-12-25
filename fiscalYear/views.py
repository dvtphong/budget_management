from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import FiscalYear
from .forms import FiscalYearForm

@login_required
def fiscal_year_list(request):
    fiscal_years = FiscalYear.objects.all()
    return render(request, 'fiscalYear/fiscal_year_list.html', {'fiscal_years': fiscal_years})

@login_required
def fiscal_year_detail(request, pk):
    fiscal_year = get_object_or_404(FiscalYear, pk=pk)
    return render(request, 'fiscalYear/fiscal_year_detail.html', {'fiscal_year': fiscal_year})

@login_required
def fiscal_year_create(request):
    if request.method == 'POST':
        form = FiscalYearForm(request.POST)
        if form.is_valid():
            fiscal_year = form.save(commit=False)
            fiscal_year.created_by = request.user
            fiscal_year.save()
            messages.success(request, 'Fiscal Year created successfully.')
            return redirect('fiscal_year:list')
    else:
        form = FiscalYearForm()
    return render(request, 'fiscalYear/fiscal_year_form.html', {'form': form, 'title': 'Create Fiscal Year'})

@login_required
def fiscal_year_update(request, pk):
    fiscal_year = get_object_or_404(FiscalYear, pk=pk)
    if request.method == 'POST':
        form = FiscalYearForm(request.POST, instance=fiscal_year)
        if form.is_valid():
            fiscal_year = form.save(commit=False)
            fiscal_year.updated_by = request.user
            fiscal_year.save()
            messages.success(request, 'Fiscal Year updated successfully.')
            return redirect('fiscal_year:list')
    else:
        form = FiscalYearForm(instance=fiscal_year)
    return render(request, 'fiscalYear/fiscal_year_form.html', {'form': form, 'title': 'Update Fiscal Year'})

@login_required
def fiscal_year_delete(request, pk):
    fiscal_year = get_object_or_404(FiscalYear, pk=pk)
    if request.method == 'POST':
        fiscal_year.delete()
        messages.success(request, 'Fiscal Year deleted successfully.')
        return redirect('fiscal_year:list')
    return render(request, 'fiscalYear/fiscal_year_confirm_delete.html', {'fiscal_year': fiscal_year})
