from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Account
from .forms import AccountForm

@login_required
def account_list(request):
    accounts = Account.objects.all()
    context = {'accounts': accounts}
    return render(request, 'account/account_list.html', context)

@login_required
def account_detail(request, pk):
    account = get_object_or_404(Account, pk=pk)
    context = {'account': account}
    return render(request, 'account/account_detail.html', context)

@login_required
def account_create(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.created_by = request.user
            account.save()
            messages.success(request, 'Account created successfully.')
            return redirect('account_list')
    else:
        form = AccountForm()
    return render(request, 'account/account_form.html', {'form': form, 'title': 'Create Account'})

@login_required
def account_update(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            account = form.save(commit=False)
            account.updated_by = request.user
            account.save()
            messages.success(request, 'Account updated successfully.')
            return redirect('account_list')
    else:
        form = AccountForm(instance=account)
    return render(request, 'account/account_form.html', {'form': form, 'title': 'Update Account'})

@login_required
def account_delete(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        account.delete()
        messages.success(request, 'Account deleted successfully.')
        return redirect('account_list')
    return render(request, 'account/account_confirm_delete.html', {'account': account})
