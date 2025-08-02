from django.contrib import admin
from vaillapp.models import Message
# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ['content', 'user', 'created_at']
admin.site.register(Message, MessageAdmin)