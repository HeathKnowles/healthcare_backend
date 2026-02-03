from django.contrib import admin

from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
	list_display = ('id', 'first_name', 'last_name', 'owner', 'date_of_birth', 'created_at')
	list_filter = ('created_at',)
	search_fields = ('first_name', 'last_name', 'email', 'phone')
