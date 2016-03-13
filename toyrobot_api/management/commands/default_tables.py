from toyrobot_api.models import *
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
	def handle(self, *args, **options):
		table=Table()
		table.name="BASE"
		Coordinates_start=Coordinates()
		Coordinates_end=Coordinates()
		Coordinates_start.name,Coordinates_start.x_cord,Coordinates_start.y_cord,Coordinates_end.name,Coordinates_end.x_cord,Coordinates_end.y_cord,=("start",0.0,0.0,"end",4.0,4.0)
		Coordinates_start.save()
		Coordinates_end.save()
		table.table_start=Coordinates_start
		table.table_end=Coordinates_end
		table.save()
		print "Success"