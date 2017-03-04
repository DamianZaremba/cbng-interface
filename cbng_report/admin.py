from django.contrib import admin

from .models import (Comment,
                     Report)

admin.site.register(Comment)
admin.site.register(Report)
