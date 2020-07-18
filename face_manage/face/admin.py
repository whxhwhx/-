from django.contrib import admin
from models import user_info, visitor_info


class user_info_admin(admin.ModelAdmin):
    list_display = ['uname', 'uphone']


class visitor_info_admin(admin.ModelAdmin):
    list_display = ['vtemp', 'vtime', 'vuser']


admin.site.register(user_info, user_info_admin)
admin.site.register(visitor_info, visitor_info_admin)
