# Generated by Django 4.2.1 on 2023-07-28 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0009_course_short_video_alter_file_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lessons",
            name="video",
            field=models.FileField(
                blank=True, null=True, upload_to="", verbose_name="video"
            ),
        ),
    ]
