# Generated by Django 4.2.7 on 2023-12-04 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_courses_course_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]