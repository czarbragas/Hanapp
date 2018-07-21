

def time_validate(self):
	cleaned_data=super(Edit_Appointment,self).clean()
	## validate time here
	if(self == None):
		return None
	return self