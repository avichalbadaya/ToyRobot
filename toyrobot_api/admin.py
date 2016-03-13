from django.contrib import admin
from models import *
# Register your models here.

class RobotAdmin(admin.ModelAdmin):
    list_display=('name','x_cord','y_cord','dirs','table',)
    

class TableAdmin(admin.ModelAdmin):
	list_display=('name','table_start','table_end',)
	

class DirectionAdmin(admin.ModelAdmin):
	list_display=('name',)

# Register your models here.
admin.site.register(Robot,RobotAdmin)
admin.site.register(Table,TableAdmin)
admin.site.register(Direction,DirectionAdmin)
admin.site.register(Coordinates)