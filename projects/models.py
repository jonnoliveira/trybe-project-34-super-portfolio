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
