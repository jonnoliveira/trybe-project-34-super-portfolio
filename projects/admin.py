from django.contrib import admin
from projects.models import (
    Certificate,
    CertifyingInstitution,
    Profile,
    Project,
)


class CertificateInline(admin.StackedInline):
    model = Certificate


class CertifyingAdmin(admin.ModelAdmin):
    inlines = [CertificateInline]


admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Certificate)
admin.site.register(CertifyingInstitution, CertifyingAdmin)
