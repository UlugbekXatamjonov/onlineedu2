# Generated by Django 4.2.1 on 2023-07-15 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0008_alter_file_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="short_video",
            field=models.TextField(blank=True, null=True, verbose_name="video EMBED"),
        ),
        migrations.AlterField(
            model_name="file",
            name="file",
            field=models.FileField(upload_to="lessons_file/%Y/%m/%d/"),
        ),
    ]