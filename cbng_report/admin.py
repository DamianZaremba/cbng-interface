from django.contrib import admin

from .models import (Beaten,
                     Comments,
                     Reports,
                     Users,
                     Vandalism)

admin.site.register(Beaten)
admin.site.register(Comments)
admin.site.register(Reports)
admin.site.register(Users)
admin.site.register(Vandalism)
