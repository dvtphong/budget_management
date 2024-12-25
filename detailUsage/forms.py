from django import forms
from detailUsage.models import DetailUsage


class DetailUsageForm(forms.ModelForm):
    class Meta:
        model = DetailUsage
        fields = ['name', 'budget_item', 'account', 'planned_amount', 'advanced_amount',
                 'settled_amount', 'remaining_amount', 'note', 'due_date']
        widgets = {
            'note': forms.Textarea(attrs={'rows': 3}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }