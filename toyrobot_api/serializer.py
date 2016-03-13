
from models import *
from rest_framework import serializers

#serializer for Robot Model
class RobotSerializer(serializers.ModelSerializer):
	direction = serializers.ReadOnlyField(source='dirs.name')
	class Meta:
		model = Robot
		fields = ('name', 'x_cord', 'y_cord','table','dirs','direction')