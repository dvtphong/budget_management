from django import forms
from budgetItem.models import BudgetItem


class BudgetItemForm(forms.ModelForm):
    class Meta:
        model = BudgetItem
        fields = ['name', 'fiscal_year', 'approved_amount', 'planned_amount',
                 'advanced_amount', 'settled_amount', 'remaining_amount', 'note']
        widgets = {
            'note': forms.Textarea(attrs={'rows': 3}),
        }