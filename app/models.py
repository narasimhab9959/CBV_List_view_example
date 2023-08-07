from django.db import models

# Create your models here.


class Trainer(models.Model):
    trainer_name=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    age=models.IntegerField()

    