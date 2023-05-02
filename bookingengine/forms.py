import calculation
from django import forms


class TestForm(forms.Form):
    quantity = forms.DecimalField()
    price = forms.DecimalField()
    amount = forms.DecimalField(
        widget=calculation.FormulaInput('quantity*price') # <- using single math expression
    )
    apply_taxes = forms.DecimalField(initial=True)
    tax = forms.DecimalField(
        # using math expression and javascript functions.
        widget=calculation.FormulaInput('apply_taxes ? parseFloat(amount/100*(apply_taxes)).toFixed(2) : 0.0') 
    )
    total = forms.DecimalField(
        # using math expression and javascript functions.
        widget=calculation.FormulaInput('apply_taxes ? parseFloat(amount + tax).toFixed(2) : 0.0') 
    )

