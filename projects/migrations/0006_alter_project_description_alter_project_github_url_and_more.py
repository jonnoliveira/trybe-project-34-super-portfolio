# Generated by Django 4.2.3 on 2023-08-29 18:51

from django.db import migrations, models
import django.db.models.deletion
import projects.validators


class Migration(migrations.Migration):
    dependencies = [
        (
            "projects",
            "0005_alter_project_description_alter_project_github_url_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.TextField(
                max_length=500, validators=[projects.validators.count_char]
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="github_url",
            field=models.URLField(validators=[projects.validators.count_char]),
        ),
        migrations.AlterField(
            model_name="project",
            name="key_skill",
            field=models.CharField(
                max_length=50, validators=[projects.validators.count_char]
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="keyword",
            field=models.CharField(
                max_length=50, validators=[projects.validators.count_char]
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="name",
            field=models.CharField(
                max_length=50, validators=[projects.validators.count_char]
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="profile",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="projects",
                to="projects.profile",
            ),
        ),
    ]
