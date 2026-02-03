from rest_framework import serializers

from doctors.models import Doctor
from doctors.serializers import DoctorSerializer
from patients.models import Patient
from .models import PatientDoctorMapping


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(
        source='patient',
        queryset=Patient.objects.all(),
        write_only=True,
    )
    doctor_id = serializers.PrimaryKeyRelatedField(
        source='doctor',
        queryset=Doctor.objects.all(),
        write_only=True,
    )

    class Meta:
        model = PatientDoctorMapping
        fields = [
            'id',
            'patient_id',
            'doctor_id',
            'doctor',
            'assigned_at',
        ]
        read_only_fields = ['id', 'doctor', 'assigned_at']
