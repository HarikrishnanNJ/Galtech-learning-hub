# Generated by Django 4.2.7 on 2023-12-04 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_course_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_description',
            field=models.CharField(blank=True, max_length=550),
        ),
    ]