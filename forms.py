# detection/forms.py
from django import forms

class TransactionForm(forms.Form):
    account_no = forms.CharField(max_length=12, label="Account Number")
    ifsc_code = forms.CharField(max_length=12, label="IFSC Code")
    amount = forms.FloatField(label="Transaction Amount")
    transaction_date = forms.DateField(label="Transaction Date (YYYY-MM-DD)")
    transaction_type = forms.ChoiceField(choices=[('credit', 'Credit'), ('debit', 'Debit')], label="Transaction Type")
