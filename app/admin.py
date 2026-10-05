from django.contrib import admin
from app.models import CustomUser,Poll,Choice

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Poll)
admin.site.register(Choice)

