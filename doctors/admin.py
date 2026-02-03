from django.contrib import admin

from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
	list_display = ('id', 'first_name', 'last_name', 'specialty', 'license_number', 'created_at')
	list_filter = ('specialty', 'created_at')
	search_fields = ('first_name', 'last_name', 'email', 'license_number')
