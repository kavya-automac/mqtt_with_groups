from django.contrib import admin
from . models import *
# Register your models here.

# class MessageAdmin(admin.ModelAdmin):
#     list_display = ["id","msg","timestamp"] # Specify the fields to display in the message list
#

admin.site.register(Message)





