from django.conf import settings
from django.db import models


class Patient(models.Model):
	owner = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name='patients',
	)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_of_birth = models.DateField()
	gender = models.CharField(max_length=20, blank=True)
	phone = models.CharField(max_length=30, blank=True)
	email = models.EmailField(blank=True)
	address = models.TextField(blank=True)
	notes = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self) -> str:
		return f"{self.first_name} {self.last_name}"
