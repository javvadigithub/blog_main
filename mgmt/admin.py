from django.contrib import admin
from .models import About

# Register your models here.
#This below class helps to remove the add button on the django admin panel
class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False

admin.site.register(About, AboutAdmin)