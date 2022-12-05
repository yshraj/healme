from django import forms
from .models import Patient_registration
from .models import Doctor_registration
from .models import Pharmacy_registration
from .models import Diagnostic_registration


class Patient_registration(forms.ModelForm):
	class Meta:
		model=Patient_registration
		fields=('fname','lname','email','gender','bloodgroup','dateofbirth','password','address')
class Doctor_registration(forms.ModelForm):
	class Meta:
		model=Doctor_registration
		fields=('fname','lname','email','gender','fees','workingdays','morningtime','eveningtime','image','speciality','experience','password','address')

class Pharmacy_registration(forms.ModelForm):
	class Meta:
		model=Pharmacy_registration
		fields=('fname','lname','email','storename','mobile','password','address')		

class Diagnostic_registration(forms.ModelForm):
	class Meta:
		model=Diagnostic_registration
		fields=('fname','lname','email','labname','mobile','password','address')		