from django import forms
from django.forms import ModelForm
from .models import Teachers2
from django.forms.widgets import TimeInput
from django.views.generic.edit import UpdateView

class UpdateData(forms.ModelForm):

	class Meta:
		model = Teachers2
		fields = ('AVAILABILITY','MOOD')

class TimeInput(forms.TimeInput):
	input_type = 'time'

class UpdateSched(forms.ModelForm):
	class Meta:
		model = Teachers2
		fields = ['Time1', 'Time2', 'Time3', 'Time4', 'Time5']
		widgets = {
			'Time1' : TimeInput(),
			'Time2' : TimeInput(),
			'Time3' : TimeInput(),
			'Time4' : TimeInput(),
			'Time5' : TimeInput()
		}


	# def clean(self):
	# 	print(self.FIRST_NAME)
	# 	Time1=self.cleaned_data['Time1']
	# 	if not Time1:
	# 		Time1 = None
	# 		return Time1
	# 	return Time1

	# 	Time2=self.cleaned_data['Time2']
	# 	if not Time2:
	# 		Time2 = None
	# 		return Time2
	# 	return Time2

	# 	Time3=self.cleaned_data['Time3']
	# 	if not Time3:
	# 		Time3 = None
	# 		return Time3
	# 	return Time3

	# 	Time4=self.cleaned_data['Time4']
	# 	if not Time4:
	# 		Time4 = None
	# 		return Time4
	# 	return Time4

	# 	Time5=self.cleaned_data['Time5']
	# 	if not Time5:
	# 		Time5 = None
	# 		return Time5
	# 	return Time5

	def save(self, commit=True):
		teachers = super(UpdateSched, self).save(commit=False)
		teachers.Time1 = self.cleaned_data['Time1']
		teachers.Time2 = self.cleaned_data['Time2']
		teachers.Time3 = self.cleaned_data['Time3']
		teachers.Time4 = self.cleaned_data['Time4']
		teachers.Time5 = self.cleaned_data['Time5']

		if commit:
			teachers.save()
		return teachers
