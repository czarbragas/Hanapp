from django.contrib import admin

# Register your models here.
from .models import Account, TangibleAsset, SoftwareAsset

admin.site.register(Account)
admin.site.register(TangibleAsset)
admin.site.register(SoftwareAsset)
