from django.db import models

from autoslug import AutoSlugField

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from = 'name', unique=True)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    comment = models.TextField()

    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Xabar")
        verbose_name_plural = ("Xabarlar")
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
