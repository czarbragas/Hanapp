from django import forms
from .models import Account


# class AccountCreateForm(forms.Form):
#     id_number   = forms.CharField()
#     fname       = forms.CharField()
#     lname       = forms.CharField()
#     password    = forms.CharField()

#     def clean_id_number(self):
#         id_number = self.cleaned_data.get("id_number")
#         if id_number == "Hello":
#             raise forms.ValidationError("Not a valid id_numebr")
#         return id_number

class AccountCreateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [ 'id_number',
                'fname',
                'lname',
                'password' ]
