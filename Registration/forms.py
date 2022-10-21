from django import forms
from .models import Employee

class FormEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["EmpRegNo", "FirstName", "LastName", "City", "Age", "MobileNo", "Email"]

