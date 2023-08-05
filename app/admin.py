from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Application


admin.site.register(Application)

admin.site.unregister(Group)