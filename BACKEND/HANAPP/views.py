from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import Teachers2, Announcements
from django.views.generic import View
from .forms import UpdateData,UpdateSched
import datetime 
from django.utils.timezone import utc


def login(request):
	return render(request,'login_page.php')


def index(request):
	DayEnd = datetime.datetime.strptime('09:00:01 PM','%I:%M:%S %p').replace(tzinfo=utc)
	DayStart = datetime.datetime.strptime('07:30:01 AM','%I:%M:%S %p')
	obj = Teachers2.objects.all()
	now = datetime.datetime.utcnow().replace(tzinfo=utc)

	if( now < DayEnd):
		obj.update(AVAILABILITY = "Not Set")
		obj.update(STATUS = "")
		
	today = datetime.datetime.utcnow().replace(tzinfo=utc)
	ann = Announcements.objects.filter(TIME_EXPIRES__gt = today)
	context = {'teachers' : obj, 'announcement': ann}
	for i in obj:
		print(i.ProfPicHappy,i.ProfPicAngry)
	return render(request, 'index.html', context)

class securityCheck(View):

	def post(self, request, *args, **kwargs):
		
		request.session['pass1'] =request.POST.get('password')
		password =match_pass(request.POST.get('password'))
		
		return  password

	def get(self, request, *args, **kwargs):
	 	obj = Teachers2.objects.all()
	 	context = {'teachers' : obj}
	 	return render(request, 'security_check.html', context)


def match_pass(inputpassword):
	teacher_list = Teachers2.objects.all()
	for obj in teacher_list:

		if(obj.SECURITY_KEY == inputpassword):
			if(obj.SECURITY_KEY == "Pass_marianne"):
				return HttpResponseRedirect('/index/signed_in_chairperson')
			return HttpResponseRedirect('/index/signed_in_index')
		
	return HttpResponseRedirect("/index/security_check")

def Signed_in(request):
	pass1 =request.session['pass1']
	today = datetime.datetime.utcnow().replace(tzinfo=utc)
	ann = Announcements.objects.filter(TIME_EXPIRES__gt = today)
	obj = Teachers2.objects.get(SECURITY_KEY =pass1)
	context = {'teachers' : obj,'announcement':ann}

	print(obj.ProfPicHappy,obj.ProfPicAngry)
	if(pass1 == "Pass_marianne"):
		return render(request, 'signed_in_chairperson.html', context)
	return render(request, 'signed_in_index.html', context)

class Edit_Status(View):

	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			availability =request.POST.get('availability')
			mood = request.POST.get('mood')
			status = request.POST.get('status')
			time = datetime.datetime.utcnow().replace(tzinfo=utc)
			teachers_obj = Teachers2.objects.filter(SECURITY_KEY__iexact=request.session["pass1"]).first()
			teachers_obj.AVAILABILITY= availability
			teachers_obj.MOOD = mood
			teachers_obj.LAST_EDITED = time
			teachers_obj.STATUS = status
			teachers_obj.save()
			if(request.session["pass1"] == "Pass_marianne"):
				return HttpResponseRedirect('/index/signed_in_chairperson')
			return HttpResponseRedirect('/index/signed_in_index')
		else:
			form = UpdateData()

		return HttpResponseRedirect('/index/signed_in_index/')

	def get(self, request, *args, **kwargs):
		pass1=request.session['pass1']
		today = datetime.datetime.utcnow().replace(tzinfo=utc)
		ann = Announcements.objects.filter(TIME_EXPIRES__gt = today)
		obj = Teachers2.objects.get(SECURITY_KEY =pass1)
		context = {'teachers' : obj,'announcement': ann}
		
		print(obj.ProfPicHappy,obj.ProfPicAngry)
		return render(request, 'edit_status.html', context)

class Add_Announcement(View):
	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			Title =request.POST.get('Title')
			Content = request.POST.get('Content')
			time_expires = request.POST.get('time_expires')
			time_posted = datetime.datetime.utcnow().replace(tzinfo=utc)
			ann_obj = Announcements.objects.create()
			ann_obj.TITLE= Title
			ann_obj.save()

			ann_obj.CONTENT= Content
			ann_obj.save()

			ann_obj.TIME_POSTED = time_posted
			ann_obj.save()
			
			ann_obj.TIME_EXPIRES = time_expires
			ann_obj.save()
			
			return HttpResponseRedirect('/index/signed_in_chairperson')
		else:
			form = UpdateData()

		return HttpResponseRedirect('/index/signed_in_chairperson/')

	def get(self, request, *args, **kwargs):
		pass1=request.session['pass1']
		today = datetime.datetime.utcnow().replace(tzinfo=utc)
		ann = Announcements.objects.filter(TIME_EXPIRES__gt = today)
		obj = Teachers2.objects.get(SECURITY_KEY =pass1)
		context = {'teachers' : obj,'announcement': ann}
	
		
		print(obj.ProfPicHappy,obj.ProfPicAngry)
		return render(request, 'add_announcement.html', context)


class Edit_Appointment(View):
	def post(self, request, *args, **kwargs):
		if request.method == 'POST':
			form = UpdateSched(request.POST)


			form.save()
			if(request.session["pass1"] == "Pass_marianne"):
				return HttpResponseRedirect('/index/signed_in_chairperson')
			return HttpResponseRedirect('/index/signed_in_chairperson')
		else:
			form = UpdateSched()

		return HttpResponseRedirect('/index/signed_in_chairperson/')

	def get(self, request, *args, **kwargs):
		pass1=request.session['pass1']
		today = datetime.datetime.utcnow().replace(tzinfo=utc)
		ann = Announcements.objects.filter(TIME_EXPIRES__gt = today)
		obj = Teachers2.objects.get(SECURITY_KEY =pass1)
		form = UpdateSched()
		context = {'teachers' : obj,'announcement': ann, 'schedEdit' : form}
		
		print(obj.ProfPicHappy,obj.ProfPicAngry)
		return render(request, 'edit_appointment_sched.html', context)


# class Request_Appointment():


class logout(View):
	def get(self, request, *args, **kwargs):
		del request.session['pass1']
		request.session.modified = True
		return HttpResponseRedirect("../index/")

class cancel(View):
	def get(self, request, *args, **kwargs):
		pass1=request.session['pass1']
		request.session.modified = True
		return HttpResponseRedirect("/index/signed_in_chairperson/")

# def Save_Status(availability,mood):
# 	pass1=request.session['pass1']
# 	obj = Teachers2.objects.filter(SECURITY_KEY =pass1)
# 	context = {'teachers' : obj}
# 	for i in obj:
# 		instance1 = Teachers2.objects.create(AVAILABILITY = availability)
# 		instance2 = Teachers2.objects.create(MOOD = mood)

# 	return render(request, 'signed_in_index.html', context)


#class updateAppontment(UpdateView)
	# model = Teachers2
	# fields['Time1'..;. 'TimeN']

