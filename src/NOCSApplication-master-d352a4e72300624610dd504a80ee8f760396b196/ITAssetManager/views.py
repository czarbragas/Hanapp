from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, CreateView
import random
# Create your views here.

from .forms import AccountCreateForm
from .models import Account
class HomeView(TemplateView):
    template_name = 'login.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        # loggedin = Account.objects.get(id = '1')
        # context.update({"loggedin" : loggedin})
        print(context)
        return context

class RegisterView(TemplateView):
    template_name = 'register.html'


class ProfileView(TemplateView):
    template_name = 'account.html'

def account_createview(request):
    form = AccountCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    if form.errors:
        errors = form.errors
        
    template_name =  'register.html'
    context = {"form" : form, "errors" : errors}
    return render(request, template_name, context)

class AccountCreateView(CreateView):
    form_class = AccountCreateForm
    template_name = 'register.html'
    success_url = "/accounts/"