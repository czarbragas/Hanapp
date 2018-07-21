"""BACKEND URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from HANAPP.views import index,securityCheck, Signed_in, Edit_Status,Add_Announcement, logout,Edit_Appointment,login,cancel
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('login/',login),
    path('admin/', admin.site.urls),
    path('index/', index),
    path('index/security_check/', securityCheck.as_view()),
    path('index/signed_in_index/', Signed_in),
    path('index/signed_in_index/edit_status/', Edit_Status.as_view()),
    path('logout/', logout.as_view()),
    path('cancel/', cancel.as_view()),
    path('index/signed_in_chairperson/', Signed_in),
    path('index/signed_in_chairperson/edit_status/', Edit_Status.as_view()),
    path('index/signed_in_chairperson/add_announcement/', Add_Announcement.as_view()),
    # path('index/signed_in_index/edit_appointment_sched/:id', UpdateAppointment.as_view()) 
    path('index/signed_in_chairperson/edit_appointment_sched/', Edit_Appointment.as_view()),
    path('index/signed_in_index/edit_appointment_sched/', Edit_Appointment.as_view())
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

