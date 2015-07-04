from django.db import models

class Qualification(models.Model):
    name = models.CharField(max_length=256)
    
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name

class Career(models.Model):
    name = models.CharField(max_length=256)
    income = models.PositiveIntegerField()
    maori_name = models.CharField(max_length=256)
    hours_worked_30_less = models.PositiveIntegerField()
    hours_worked_60_less = models.PositiveIntegerField()
    hours_worked_60_more = models.PositiveIntegerField()

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name

class Interests(models.Model):
    name = models.CharField(max_length=256)
    careers = models.ManyToManyField(Career)
    maori_name = models.CharField(max_length=256)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name