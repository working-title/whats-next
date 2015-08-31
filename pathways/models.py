from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from taggit.managers import TaggableManager


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
    no_qualification = models.PositiveIntegerField(default=0)
    school = models.PositiveIntegerField(default=0)
    post_school = models.PositiveIntegerField(default=0)
    degree = models.PositiveIntegerField(default=0)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name


class Industry(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    careers = models.ManyToManyField(Career)
    tags = TaggableManager()

    class Meta:
        verbose_name_plural = "industries"

    def __unicode__(self):
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

    class Meta:
        verbose_name_plural = "categories"

    def __unicode__(self):              # __unicode__ on Python 2
        return self.name
