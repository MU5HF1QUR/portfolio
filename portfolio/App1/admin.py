from django.contrib import admin
from . models import contactInfo

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')

admin.site.register(contactInfo, ContactAdmin)
