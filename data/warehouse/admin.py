from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import *

admin.site.register(Group, SimpleHistoryAdmin)
admin.site.register(Post, SimpleHistoryAdmin)