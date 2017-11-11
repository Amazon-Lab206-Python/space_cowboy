# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

<<<<<<< HEAD
class DojoManager(models.Manager):
    def dojos_city_must_not_be_blank_validation(self, postData):
        errors = []
        if postData['city'] == "":
            errors.append("city cannot be empty string")
        if len(errors) == 0:
            d = Dojo.objects.create(city=postData['city'], state=postData['state'])
            return [True, d]
        else:
            return [False, False]

=======
>>>>>>> 144a8482319f5d16d72944556782b98b4e198ad6
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField()
<<<<<<< HEAD
    
    objects = DojoManager()

    def __unicode__(self):
        return "name:" + self.name + ", location: " + self.city + ", state: " + self.state
=======
>>>>>>> 144a8482319f5d16d72944556782b98b4e198ad6

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
<<<<<<< HEAD
    dojo = models.ForeignKey(Dojo, related_name="ninjas")

    def __unicode__(self):
        return "first name:" + self.first_name + ", last_name: " + self.last_name + ", dojo: " + self.dojo
=======
    dojo = models.ForeignKey(Dojo, related_name="ninjas")
>>>>>>> 144a8482319f5d16d72944556782b98b4e198ad6
