import datetime

from django.db import models

class Inproduct(models.Model):
    kg = "kg"
    tonna = "tonna"
    gramm = "gramm"
    litr = "litr"
    metr = "metr"
    sm = "santimetr"
    dona = "dona"
    ROLES = (
        (kg,"kg"),
        (tonna,"tonna"),
        (gramm,"gramm"),
        (litr,"litr"),
        (metr,"metr"),
        (sm,"sm"),
        (dona,"dona"),
    )
    name = models.CharField(max_length=512)
    inload_number = models.CharField(max_length=200)
    count = models.FloatField(default=0)
    instorageperson=models.CharField(max_length=200)
    takeinstorageperson=models.CharField(max_length=200)
    unit = models.CharField(max_length=30,choices=ROLES)
    in_date = models.DateTimeField(default=datetime.datetime.now())
    class Meta:
        db_table = "Inproduct"

    def __str__(self):
        return f"{self.name}--{self.count}--{self.instorageperson}--{self.takeinstorageperson}--{self.unit}--{self.in_date}"
class Outproduct(models.Model):
    name = models.CharField(max_length=512)
    receiver_name = models.CharField(max_length=200)
    outload_number = models.CharField(max_length=200)
    outstorageperson = models.CharField(max_length=200)
    getinstorageperson = models.CharField(max_length=200)
    count = models.FloatField(default=0)
    unit = models.CharField(max_length=30,choices=Inproduct.ROLES)
    out_date = models.DateTimeField(default=datetime.datetime.now())
    class Meta:
        db_table = "Outproduct"
    def __str__(self):
        return f"{self.name}--{self.count}"

class BalanceStorage(models.Model):
    name = models.CharField(max_length=512)
    count = models.FloatField(default=0)
    unit = models.CharField(max_length=30,choices=Inproduct.ROLES)
    class Meta:
        db_table = "BalanceStorage"
    def __str__(self):
        return f"{self.name}--{self.count}--{self.unit}"