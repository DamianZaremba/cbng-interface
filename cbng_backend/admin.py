from django.contrib import admin

from .models import (Beaten,
                     Vandalism)

admin.site.register(Beaten)
admin.site.register(Vandalism)
