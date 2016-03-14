django-Toy-Robot
==================

A Django App that exposes REST Api's for running a Toy Robot on a given Table. This app is designed to support following features:

1. Add a new Robot
2. Position a Existing Robot
3. Move a Robot in certain direction
4. Rotate a Robot direction left or Right
5. Api's support CORS (Cross-Origin Resource Sharing).

## Setup ##
Install required python packages by downloading the source and running:

>   pip install -r requirements.txt

Run Django app locally by following command

>   python manage.py runserver 0.0.0.0:8000

## If you are using your own database and not existing sqlite3 then:
- Add DB configuration to /ToyRobot/settings.py file
- Also run following commands to prepare Database

>   python manage.py makemigrations

>   python manage.py migrate

>   python manage.py default_tables //to create Directions NORTH,EAST,SOUTH,WEST and Table BASE 

# Deploy it on Heroku

## Prerequisits
- Heroku toolbelt - install it from https://toolbelt.heroku.com/

## Steps
- Go inside SlackBot project folder
- run following commands

```shell
heroku login
heroku create
git push heroku master
heroku ps:scale web=1
heroku open
```


# API List

## GET list of Robots- GET /robot/

>   CURL -i http://127.0.0.1:8000/robot/

Sample output
```shell
HTTP/1.0 200 OK
....
[{"name":"ROBOT_5","x_cord":4.0,"y_cord":4.0,"table":3,"dirs":6,"direction":"EAST"},{"name":"ROBOT_6","x_cord":3.0,"y_cord":4.0,"table":3,"dirs":6,"direction":"EAST"}]
```

## Add New Robot- POST /<ROBOT_NAME>
>   CURL -X POST -i http://127.0.0.1:8000/robot/ROBOT_7/

Sample output
```shell
HTTP/1.0 201 Created
...
{"name":"ROBOT_7","x_cord":null,"y_cord":null,"table":null,"dirs":null,"direction":null}
```

## Position Robot- POST /<ROBOT_NAME>/position/ -d '{"angle":"WEST", "x_pos":2, "y_pos":2}'
>   CURL -X POST -i http://127.0.0.1:8000/robot/ROBOT_7/position/ -H "Content-type: application/json" -d '{"angle":"WEST", "x_pos":2, "y_pos":2}'

Sample output
```shell
HTTP/1.0 201 Created
...
{"name":"ROBOT_7","x_cord":2.0,"y_cord":2.0,"table":3,"dirs":5,"direction":"WEST"}
```

## Get Details about a Robot - GET /robot/<ROBOT_NAME>/
>   CURL -i http://127.0.0.1:8000/robot/ROBOT_7/

Sample output
```shell
HTTP/1.0 200 OK
...
{"name":"ROBOT_7","x_cord":1.0,"y_cord":2.0,"table":3,"dirs":8,"direction":"WEST"}
```

## Move Robot in direction of its facing - PUT /robot/<ROBOT_NAME>/move/
>   CURL -X PUT -i http://127.0.0.1:8000/robot/ROBOT_7/move/

Sample output
```shell
HTTP/1.0 201 Created
...
{"name":"ROBOT_7","x_cord":1.0,"y_cord":2.0,"table":3,"dirs":5,"direction":"WEST"}
```

## Rotate Robot left - PUT /robot/<ROBOT_NAME>/left/
>   CURL -X PUT -i http://127.0.0.1:8000/robot/ROBOT_7/left/

Sample output
```shell
HTTP/1.0 201 Created
...
{"name":"ROBOT_7","x_cord":1.0,"y_cord":2.0,"table":3,"dirs":8,"direction":"SOUTH"}
```

## Rotate Robot right - PUT /robot/<ROBOT_NAME>/right/
>   CURL -X PUT -i http://127.0.0.1:8000/robot/ROBOT_7/right/

Sample output
```shell
HTTP/1.0 201 Created
...
{"name":"ROBOT_7","x_cord":1.0,"y_cord":2.0,"table":3,"dirs":8,"direction":"WEST"}
```
