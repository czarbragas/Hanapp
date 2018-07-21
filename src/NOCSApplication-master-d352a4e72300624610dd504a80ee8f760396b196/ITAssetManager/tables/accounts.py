from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
import random
from ..models import Account
# Create your Account Model functions here.


class AccountListView(ListView):
    template_name = "account_list.html"
    def get_queryset(self):
        print(self.kwargs)
        searchkey = self.kwargs.get('slug')
        if searchkey:
            queryset = Account.objects.filter(id_number__icontains=searchkey)
        else:
            queryset = Account.objects.all()
        return queryset

class AccountDetailView(DetailView):
    queryset = Account.objects.all()
    template_name = "account_detail.html"

    def get_context_data(self, *args, **kwargs):
        print(self.kwargs)
        context = super(AccountDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    # def get_object(self, *args, **kwargs):
    #     account_id = self.kwargs.get('account_id')
    #     obj = get_object_or_404(Account,id=account_id)
    #     return obj 