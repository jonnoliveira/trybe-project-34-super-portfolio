# Generated by Django 4.2.3 on 2023-08-29 20:12

from django.db import migrations, models
import projects.validators


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0008_alter_certificate_profiles"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificate",
            name="timestamp",
            field=models.DateTimeField(
                auto_now_add=True, validators=[projects.validators.count_char]
            ),
        ),
    ]
