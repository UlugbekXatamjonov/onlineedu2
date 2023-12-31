# Generated by Django 4.2.1 on 2023-07-15 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0003_teacher_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="courses",
                to="course.coursecategory",
            ),
        ),
        migrations.AlterField(
            model_name="file",
            name="file",
            field=models.FileField(upload_to="lesson_file/"),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="photo",
            field=models.ImageField(
                blank=True,
                default="default_photos/teacher_photo.png",
                null=True,
                upload_to="teachers_photo/%Y/%m/%d/",
                verbose_name="Rasm",
            ),
        ),
    ]
