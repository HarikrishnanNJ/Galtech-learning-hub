# Generated by Django 4.2.7 on 2023-12-11 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_courses_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='home.lessons'),
        ),
        migrations.AlterField(
            model_name='video',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(upload_to='unique_name', verbose_name='Thumbnail'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(upload_to='videos/', verbose_name='Video file'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_upload_url',
            field=models.URLField(max_length=250, verbose_name='Video URL'),
        ),
    ]
