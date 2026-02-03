from django.shortcuts import get_object_or_404
from rest_framework import permissions, response, status, viewsets
from rest_framework.exceptions import PermissionDenied

from patients.models import Patient
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer


class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
	queryset = PatientDoctorMapping.objects.select_related('doctor', 'patient')
	serializer_class = PatientDoctorMappingSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		return self.queryset.filter(patient__owner=self.request.user)

	def retrieve(self, request, *args, **kwargs):
		patient_id = kwargs.get('pk')
		patient = get_object_or_404(Patient, pk=patient_id, owner=request.user)
		mappings = self.get_queryset().filter(patient=patient)
		serializer = self.get_serializer(mappings, many=True)
		return response.Response(serializer.data, status=status.HTTP_200_OK)

	def perform_create(self, serializer):
		patient = serializer.validated_data.get('patient')
		if patient.owner != self.request.user:
			raise PermissionDenied('You do not have permission to assign doctors to this patient.')
		serializer.save()
