from rest_framework import status
from rest_framework.test import APITestCase
from models import *

class RobotList(APITestCase):
    def test_robot_list(self):
        """
        Ensure that we can get robot list from /robot
        """
        self.client.post('/robot/new_robot/')
        self.client.post('/robot/another_robot/')
        response = self.client.get('/robot/')
        print response
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CreateRobot(APITestCase):
    def test_robot_creation(self):
        """
        Ensure that we can create robot and also do not overwrite existing robot
        """
        response = self.client.post('/robot/hol_robot/')
        try_duplicate=self.client.post('/robot/hol_robot/')
        print response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(try_duplicate.status_code, status.HTTP_303_SEE_OTHER)

class PositionRobot(APITestCase):
	def test_robot_position(self):
		"""
		Ensure that we can position a robot in default Base table
		"""
		PrepareDefault()
		response = self.client.post('/robot/new_robot/')
		data = {"angle":"WEST", "x_pos":2, "y_pos":2}
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		response = self.client.post('/robot/new_robot/position/', data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

def PrepareDefault():
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

	directions={"NORTH":1.0,"EAST":0.5,"SOUTH":0,"WEST":1.5}
	for key,value in directions.iteritems():
		dirs=Direction()
		dirs.name=key
		dirs.facing=value
		dirs.save()

