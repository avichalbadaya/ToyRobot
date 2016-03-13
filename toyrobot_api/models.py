from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Coordinates(models.Model):
	def __unicode__(self):
		return self.name
	name = models.CharField(max_length=100,unique=True)
	x_cord = models.FloatField()
	y_cord = models.FloatField()

class Table(models.Model):
	def __unicode__(self):
		return self.name
	name = models.CharField(max_length=100,unique=True)
	table_start  = models.ForeignKey(Coordinates,related_name='table_start')
	table_end  = models.ForeignKey(Coordinates,related_name='table_end')

class Direction(models.Model):
	def __unicode__(self):
		return self.name
	name = models.CharField(max_length=100,unique=True)
	facing = models.FloatField()

class Robot(models.Model):
    def __unicode__(self):
        return self.name
    name=models.CharField(max_length=100,unique=True)
    x_cord = models.FloatField(null=True)
    y_cord = models.FloatField(null=True)
    table = models.ForeignKey(Table,related_name="Name",null=True)
    dirs = models.ForeignKey(Direction,related_name="Name",null=True)