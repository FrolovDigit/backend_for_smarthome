from django.contrib import admin
#from .models import Channel
#, Log
#####
#admin.site.register(Channel)
# Register your models here.
@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name','min', 'max','type')
@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('kanal','value','time')
