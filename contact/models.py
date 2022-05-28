from django.db import models

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=50, verbose_name="Oggetto")
    msg_body = models.TextField(max_length=200, verbose_name="Contenuto")
