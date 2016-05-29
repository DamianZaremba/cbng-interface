from django.contrib import admin

from .models import (Beaten,
                     Comment,
                     Report,
                     User,
                     Vandalism)

admin.site.register(Beaten)
admin.site.register(Comment)
admin.site.register(Report)
admin.site.register(User)
admin.site.register(Vandalism)
