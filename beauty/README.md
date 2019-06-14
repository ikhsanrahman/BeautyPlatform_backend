## Beauty Platform Backend

Beauty Platform Backend is a Backend API that can process everything behind. this system has been created more flexible and scalable, so the developer can use and modify this api as flexible as possible they want.

# Brief Introduction

This system API is going to use Docker to run the apps. Docker is used to make it easily in maintanance. This system will process anything related to bussiness requirement.  

# Tech used
This system uses python as core tech and Postgresql as Database Management System (DBMS). for more details, please see in requirements.txt for all
dependencies being used. several framework used as follow :
1. flask-resplus
2. flask-marshmallow
3. flask-sqlalchemy
4. fask-migrate
5. flask-cors
6. JWT for authentication (soon)
7. etc

## Usage 
 
1. clone the repository and put where ever directory you wanna put in virtual machine
2. make and activate the virtual environment to isolate and wrap the application and prevent something that will distract and disturb also
3. install docker and docker compose in your virtual machine
4. create database first. in Command Line Interface. by the way, i use linux as core OS.
	``` sudo -i -u postgres psql ```
	``` CREATE DATABASE db_beauty_dev;``` for development
	``` CREATE USER beauty WITH ENCRYPTED PASSWORD 'beauty';``` for creating authentication in Database
5. then, install all dependencies in requirements.txt. type ``` pip install requirements.txt```
6. then, migrate the data to database. type ``` make init ```, ``` make mig ```, ``` make upg ```   
7. run application using command as follow
		``` make run ``` this works in linux mint 19.0.1. but still worry whether works in other Operating System.

## API endpoint

This api use port [6000] and prefix [/api/v1]. to run must add these parts to url when start. to run properly, 
add this endpoints to the url. they are :

1. Home URL. this url is a Home page of Beauty Platform API. use [GET] method.
	``` .../api/v1/ ``` 
2. Create a New Field. this url uses [POST] method. the last slash need to involve.
	``` .../fields ``` 
3. Edit Field. this url uses [PUT] method. the last slash need to involve
	``` .../fields ```
4. Delete Field. this url uses [DELETE] method. the last slash need to involve
	``` ...fields ```
5. Re-Activate Field. this url uses [POST] method. 
	``` ...fields/activate ```
6. Get All Fields. this url uses [GET] method
	``` ...fields ```
7. Get One Field. this url uses [POST] method. need to complete the form.
	``` .../fields/searchField ```
8. Get Dummy Token. this token is used to generate token to activate other APIs.
	``` .../fields/login ```
9. Remove a Field from database. this url uses ['POST'] method to remove a field from database
   ``` ..../fields/remove ```
10. Score every field that has been registered. use [GET method to score fields.
   ``` .../score ```
	
## Creating all Fields in one Script

the All fields has been provided and can be made in using one script only. List of all fields can be seen in directory create_all_field/data.py. to make all fields that is already provided, just run the create_field.py script using command as follow :
``` python create_field.py ```

it will directly make all fields in one function