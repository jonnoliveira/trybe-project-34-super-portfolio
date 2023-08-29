# Generated by Django 4.2.3 on 2023-08-29 20:47

from django.db import migrations, models
import django.db.models.deletion
import projects.validators


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0011_alter_certificate_profiles"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificate",
            name="certifying_institution",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="certificates",
                to="projects.certifyinginstitution",
                validators=[projects.validators.count_char],
            ),
        ),
    ]
