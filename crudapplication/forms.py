from django import forms
from .models import Employee
# employee form field can be added


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
