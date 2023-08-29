from rest_framework import serializers
from projects.models import CertifyingInstitution, Certificate


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = (
            "id",
            "name",
            "certifying_institution",
            "timestamp",
            "profiles",
        )


class NestedCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = (
            "id",
            "name",
            "profiles",
            "timestamp",
        )


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = NestedCertificateSerializer(many=True, required=False)

    class Meta:
        model = CertifyingInstitution
        fields = ("id", "name", "url", "certificates")

    def create(self, validated_data):
        certificates_data = validated_data.pop("certificates", [])
        institution = CertifyingInstitution.objects.create(**validated_data)

        for certificate_data in certificates_data:
            Certificate.objects.create(
                certifying_institution=institution, **certificate_data
            )
        return institution
