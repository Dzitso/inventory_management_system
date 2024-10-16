from django.shortcuts import render, redirect, get_object_or_404
from .models import Asset
from .forms import AssetForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.db.models import Q
def home(request):
    return render(request, 'home.html')
@login_required
def asset_list(request):
    assets = Asset.objects.all()
    search_query = request.GET.get('search_query', '')

    if search_query:
        assets = assets.filter(
            Q(asset_type__icontains=search_query) |
            Q(name__icontains=search_query) |
            Q(model__icontains=search_query) |
            Q(department__icontains=search_query) |
            Q(owner__icontains=search_query) |
            Q(status__icontains=search_query)
        )

    context = {
        'assets': assets,
        'search_query': search_query,
    }
    return render(request, 'asset_list.html', context)
def asset_create(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('inventory:asset_list'))
    else:
        form = AssetForm()
    return render(request, 'asset_form.html', {'form': form})

def asset_update(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return render(request, 'asset_list.html')
    else:
        form = AssetForm(instance=asset)
    return render(request, 'asset_form.html', {'form': form})

def asset_delete(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        asset.delete()
        return render(request, 'asset_list.html')
    return render(request, 'asset_confirm_delete.html', {'asset': asset})
