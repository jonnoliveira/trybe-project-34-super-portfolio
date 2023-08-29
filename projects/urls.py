from django.urls import path, include
from rest_framework import routers
from projects.views import (
    CertificateViewSet,
    CertifyingViewSet,
    ProfileViewSet,
    ProjectViewSet,
)

router = routers.DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"projects", ProjectViewSet)
router.register(r"certifying-institutions", CertifyingViewSet)
router.register(r"certificates", CertificateViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
