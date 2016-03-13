from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from models import Robot,Table,Direction
from serializer import *
from rest_framework import status
from math import pi,sin,cos

#RobotList APIView is used to respond back list of all robots
class RobotList(APIView):
    """
    List all robots
    """
    def get(self, request, format=None):
    	robots = Robot.objects.all()
    	serializer = RobotSerializer(robots, many=True)
        return Response(serializer.data)

#Robot detail APIView which can be used to get/update/create robots
class RobotDetail(APIView):
    """
    Get/Create/Update robots
    """
    def get_object(self, pk):
        try:
            return Robot.objects.get(name=pk)
        except Robot.DoesNotExist:
        	return None

    def get(self, request, pk,move=None, format=None):
    	try:
    		print pk
        	robot = self.get_object(pk)
        	serializer = RobotSerializer(robot)
        	direction=Direction.objects.get(id=serializer.data['dirs'])
        	return Response(serializer.data)
        except:
        	return Response({})

    def post(self, request, pk,move=None,format=None):
    	robot = self.get_object(pk)
    	if(robot==None):
    		CreateRobot(pk)
    		robot = self.get_object(pk)
    		serializer = RobotSerializer(robot)
    		return Response(serializer.data, status=status.HTTP_201_CREATED)
    	else:
    		print move
    		if(move==None):
    			serializer = RobotSerializer(robot)
    			return Response(serializer.data, status=status.HTTP_303_SEE_OTHER)
    		elif(move=='position'):
    			print "HERE"
    			table=Table.objects.get(name="BASE")
    			direction=Direction.objects.get(name=request.data["angle"])
    			robot.table,robot.dirs,robot.x_cord,robot.y_cord=(table,direction,request.data["x_pos"],request.data["y_pos"])
    			robot.save()
    			serializer = RobotSerializer(robot)
    			return Response(serializer.data, status=status.HTTP_201_CREATED)
    		else:
    			serializer = RobotSerializer(robot)
    			return Response(serializer.data, status=status.HTTP_304_NOT_MODIFIED)


    def put(self, request,pk,move=None,format=None):
        robot = self.get_object(pk)
        serializer = RobotSerializer(robot)
        if(robot.table is not None):
        	move_status=MoveRobot(robot,move)
        	serializer = RobotSerializer(robot)
        	if(move_status):
        		return Response(serializer.data, status=status.HTTP_201_CREATED)
        	else:
        		return Response(serializer.data,status=status.HTTP_304_NOT_MODIFIED)
        else:
        	return Response(serializer.data,status=status.HTTP_304_NOT_MODIFIED)

#Function to create Robot which is not placed on table
def CreateRobot(name):
	robot=Robot()
	robot.name,robot.table,robot.dirs,robot.x_cord,robot.y_cord=(name,None,None,None,None)
	robot.save()
	return

#function to move robot either in direction it is facing or rotate left or right. 
def MoveRobot(robot,move):
	if(move=='left'):
		direc=Direction.objects.get(facing=(robot.dirs.facing + 0.5)%2)
		robot.dirs=direc
		robot.save()
		return True
	elif(move=='right'):
		direc=Direction.objects.get(facing=(robot.dirs.facing - 0.5)%2)
		robot.dirs=direc
		robot.save()
		return True
	elif(move=='move'):
		x_cord=robot.x_cord+round(sin(pi * robot.dirs.facing))
		y_cord=robot.y_cord+round(cos(pi * robot.dirs.facing))
		if CheckTable(x_cord,y_cord,robot.table):
			robot.x_cord=robot.x_cord+round(sin(pi * robot.dirs.facing))
			robot.y_cord=robot.y_cord+round(cos(pi * robot.dirs.facing))
			robot.save()
			return True
	else:
		return False
#function to check if given coordinates are present in table or not
def CheckTable(x_cord,y_cord,table):
	return x_cord <= table.table_end.x_cord and x_cord >= table.table_start.x_cord and y_cord <= table.table_end.y_cord and y_cord >= table.table_start.y_cord
