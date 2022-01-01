from django.contrib import admin
from .models import Customer
from django.contrib.auth.models import User
import pprint
from django.contrib.sessions.models import Session


class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']

admin.site.register(Session, SessionAdmin)

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    models = Customer
    list_display = ['id','first_name','last_name','phone_no','email_id','password1','password2']



admin.site.register(Customer,CustomerAdmin)