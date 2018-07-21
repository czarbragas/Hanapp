from django.db import models
from django.db.models.signals import pre_save, post_save
# Create your models here.

from .utils import unique_slug_generator
class Account(models.Model):
    id_number   = models.CharField(max_length=15)
    fname       = models.CharField(max_length=30, null = True, blank = False)
    lname       = models.CharField(max_length=30, null = True, blank = False)
    password    = models.CharField(max_length=30, null = True, blank = False)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(null = True, blank = True)

    def __str__(self):
        return self.id_number + " " + self.fname + " " + self.lname 

    @property
    def title(self):
        return self.fname + " " + self.lname + " " + self.id_number 

def accpre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        

# def accpost_save_receiver(sender, instance, created,  *args, **kwargs):
#     print('saved')
#     print(instance.timestamp)
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#         instance.save()


pre_save.connect(accpre_save_receiver, sender=Account)

# post_save.connect(accpost_save_receiver, sender=Account)

class Asset(models.Model):
    name            = models.CharField(max_length = 100, null = False, blank = False)
    department      = models.CharField(max_length=100, null = False, blank = False)
    property_no     = models.CharField(max_length=100, null = False, blank = False)
    purchase        = models.DateField()
    STATUS          = (('D', 'Deployed'),
                       ('U', 'Undeployed')
                      )
    status          = models.CharField(max_length=1, choices=STATUS)
    warranty_date   = models.DateField()
    purchase_cost   = models.FloatField()
    brand           = models.CharField(max_length = 100, null = False, blank = False)
    timestamp       = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    slug            = models.SlugField(null = True, blank = True)

    class Meta:
        abstract = True


class TangibleAsset(Asset):
    model_no            = models.CharField(max_length=50, null = False, blank = False)
    serial_no           = models.CharField(max_length=100, null = False, blank = False)
    termination_date    = models.DateField()

    def __str__(self):
        return self.name + " " + self.brand + " TANGIBLE"

class SoftwareAsset(Asset):
    expiration_date     = models.DateField()
    license_key         = models.CharField(max_length=100, null = False, blank = False)

    def __str__(self):
        return self.name + " " + self.brand + " SOFTWARE"


