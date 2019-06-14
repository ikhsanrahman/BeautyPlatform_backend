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
5. then, install all dependencies in requirements.txt. type ``` pip install -r requirements.txt```
6. then, migrate the data to database. type ``` make init ```, ``` make mig ```, ``` make upg ```   
7. run application using command as follow
		``` make run ``` this works in linux mint 19.0.1. but still worry whether works in other Operating System.

## API endpoint

This api use port [6000] and prefix [/api/v1]. to run must add these parts to url when start. to run properly, 
add this endpoints to the url. they are :

1. Home URL. this url is a Home page of Beauty Platform API. use [GET] method.
	``` .../api/v1/ ``` 
2. Login Buyer. this url uses [GET] method. the last slash need to involve.
	``` .../api/v1/buyer/login ``` 
3. Search Buyer. this url uses [GET] method. the last slash need to involve
	``` .../api/v1/buyer/search ```
4. Get All Buyers. this url uses [Get] method.
	``` .../api/v1/buyer/```
5. Register new buyer. this url uses [POST] method. 
	``` .../api/v1/buyer/```
6. Forget Password Buyer. this url uses [PUT] method
	``` .../api/v1/buyer/ ```
7. Update Profile Buyer. this url uses [PUT] method. need to complete the form.
	``` .../api/v1/buyer/<id-buyer>```
8. Remove a Buyer. the used method is delete.
	``` .../api/v1/buyer/<id-buyer>```
9. Update password that buyer own. the method is [PUT]
   ``` ..../api/v1/buyer/<id-buyer>/updatepassword```
10. Unactivate buyer. the method is [GET].
   ``` .../api/v1/buyer/<id-buyer>/unactivate```

11. re-activate buyer. the method is [GET].
   ``` .../api/v1/buyer/<id-buyer>/reactivate```
	
