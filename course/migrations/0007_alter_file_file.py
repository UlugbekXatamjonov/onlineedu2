# Generated by Django 4.2.1 on 2023-07-15 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0006_alter_file_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="file",
            name="file",
            field=models.FileField(upload_to="lessons_file/{self.slug}/"),
        ),
    ]