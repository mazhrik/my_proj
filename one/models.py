from django.db import models


# Create your models here.


class engine_model(models.Model):
    cc = models.IntegerField()
    color = models.CharField(max_length=30)


class car_model(models.Model):
    name = models.CharField(max_length=30)
    model_no = models.IntegerField()
    _new = models.OneToOneField(engine_model, on_delete=models.CASCADE, null=True)


class department(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30,null=True)


class employee(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    _info = models.ForeignKey(department, on_delete=models.CASCADE, null=True)
