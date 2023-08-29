# Generated by Django 4.2.3 on 2023-08-29 19:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0007_certifyinginstitution_certificate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificate",
            name="profiles",
            field=models.ManyToManyField(
                default=2, related_name="certificates", to="projects.profile"
            ),
        ),
    ]