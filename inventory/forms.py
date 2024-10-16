from django import forms
from .models import Asset

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['asset_type', 'name', 'model', 'department', 'owner', 'last_maintenance', 'status', 'specifications']
        widgets = {
            'last_maintenance': forms.DateInput(attrs={'type': 'date'}),}
        