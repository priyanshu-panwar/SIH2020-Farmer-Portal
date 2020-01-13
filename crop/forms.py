from django import forms
from .models import Crop

class CropForm(forms.ModelForm):
	class Meta:
		model = Crop
		fields = ('cat', 'name', 'quantity', 'unit', 'description', 'pickup', 'image')
