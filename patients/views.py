from rest_framework import permissions, viewsets

from .models import Patient
from .serializers import PatientSerializer


class IsOwner(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.owner == request.user


class PatientViewSet(viewsets.ModelViewSet):
	serializer_class = PatientSerializer
	permission_classes = [permissions.IsAuthenticated, IsOwner]

	def get_queryset(self):
		return Patient.objects.filter(owner=self.request.user)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
