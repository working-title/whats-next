from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Qualification(models.Model):
    name = models.CharField(max_length=256)
    debt = models.FloatField(default=0, validators=[MinValueValidator(0)])

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name

class Career(models.Model):
    name = models.CharField(max_length=256)
    income = models.PositiveIntegerField()
    qualifications = models.ManyToManyField(Qualification)
    maori_name = models.CharField(max_length=256, blank=True)
    hours_worked_30_less = models.PositiveIntegerField()
    hours_worked_60_less = models.PositiveIntegerField()
    hours_worked_60_more = models.PositiveIntegerField()

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name


class Interest(models.Model):
    name = models.CharField(max_length=256)
    careers = models.ManyToManyField(Career)
    maori_name = models.CharField(max_length=256, blank=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=256)
    interests = models.ManyToManyField(Interest)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name
