from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomAdmin(UserAdmin):
    list_display=('email','first_name','last_name','username','last_login','is_active','date_joined','role')
    filter_horizontal =()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, CustomAdmin)

