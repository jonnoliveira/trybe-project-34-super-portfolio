from django.db import models
from projects.validators import count_char


class Profile(models.Model):
    name = models.CharField(
        max_length=100, null=False, validators=[count_char]
    )
    github = models.URLField(
        max_length=200, null=False, validators=[count_char]
    )
    linkedin = models.URLField(
        max_length=200, null=False, validators=[count_char]
    )
    bio = models.TextField(null=False, validators=[count_char])

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50, validators=[count_char])
    description = models.TextField(max_length=500, validators=[count_char])
    github_url = models.URLField(validators=[count_char])
    keyword = models.CharField(max_length=50, validators=[count_char])
    key_skill = models.CharField(max_length=50, validators=[count_char])
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="projects",
        default=2,
    )

    def __str__(self):
        return self.name


class CertifyingInstitution(models.Model):
    name = models.CharField(max_length=100, validators=[count_char])
    url = models.URLField(validators=[count_char])

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(
        max_length=100, validators=[count_char], null=False
    )
    certifying_institution = models.ForeignKey(
        CertifyingInstitution,
        on_delete=models.CASCADE,
        related_name="certificates",
        default=2,
        null=False,
    )
    timestamp = models.DateTimeField(
        validators=[count_char], auto_now_add=True
    )
    profiles = models.ManyToManyField(
        Profile,
        related_name="certificates",
        default=2,
    )

    def __str__(self):
        return self.name
