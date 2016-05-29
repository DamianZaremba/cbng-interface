from django.contrib import admin

from .models import (Edit,
                     EditGroup,
                     Classification)

admin.site.register(Edit)
admin.site.register(EditGroup)
admin.site.register(Classification)