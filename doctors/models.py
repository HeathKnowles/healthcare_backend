from django.db import models


class Doctor(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	specialty = models.CharField(max_length=120)
	license_number = models.CharField(max_length=50, unique=True)
	years_experience = models.PositiveIntegerField(default=0)
	phone = models.CharField(max_length=30, blank=True)
	email = models.EmailField(blank=True)
	bio = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['last_name', 'first_name']

	def __str__(self) -> str:
		return f"Dr. {self.first_name} {self.last_name}"
