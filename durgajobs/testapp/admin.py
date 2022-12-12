from django.contrib import admin
from testapp.models import Hydjobs,Bangalorejobs,Punejobs

# Register your models here.
class HydjobsAdmin(admin.ModelAdmin):
    list_diplay = ['date','company','title','eligibility','address','email','phonenumber']

admin.site.register(Hydjobs,HydjobsAdmin)


class BangalorejobsAdmin(admin.ModelAdmin):
    list_diplay = ['date','company','title','eligibility','address','email','phonenumber']

admin.site.register(Bangalorejobs,BangalorejobsAdmin)


class PunejobsAdmin(admin.ModelAdmin):
    list_diplay = ['date','company','title','eligibility','address','email','phonenumber']

admin.site.register(Punejobs,PunejobsAdmin)
