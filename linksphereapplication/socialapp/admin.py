from django.contrib import admin

# Register your models here.

from socialapp.models import Stories,Posts

admin.site.register(Posts)
admin.site.register(Stories)
