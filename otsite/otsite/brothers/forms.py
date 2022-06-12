from django import forms
from .models import Brother

class BrotherCreateForm(forms.ModelForm):
    graduation_year = forms.IntegerField(initial=2025, required=True)
    email = forms.EmailField()
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    major = forms.CharField(required=True)
    
    class Meta:
        model = Brother
        fields = [
            'first_name',
            'last_name',
            'email',
            'major',
            'graduation_year'
        ]

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("bu.edu"):
            raise forms.ValidationError("Please enter BU email")
        return email
