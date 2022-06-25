## How to create new database and connect to project
 - Install MySql Server 

 During the initial setup, Django creates the project tables but cannot create the database. To have a usable project we need the database credentials used later by the Django project. The database can be created visually using a database tool (like MySQL Workbench) or using the terminal:
```
CREATE DATABASE mytestdb;
```
- Create a new MySql user and set your param in .env file
```
CREATE USER 'test'@'localhost' IDENTIFIED BY 'Secret_1234';
```
- Grant all privileges to the newly created user
``` 
GRANT ALL PRIVILEGES ON `mytestdb` . * TO 'test'@'localhost';
FLUSH PRIVILEGES; 
```

## Start the project
```
pip install -r requirements.txt
```
The next step is to run the Django migration that will create all necessary tables.
```
python manage.py makemigrations
python manage.py migrate
```
Start the project
``` 
python manage.py collectstatic
python manage.py runserver
```

## API Endpoints
- Select all Doctors or Specialties:
``` 
http://127.0.0.1:8000/restapi/specialties/  - # all specialties
http://127.0.0.1:8000/restapi/doctors/  - # all doctors
```
- Select current doctor or specialty

You have simple CRUD(UPDATE or DELETE) operations with current item
```
http://127.0.0.1:8000/doctor/<doctorname-number_of_sort>/
http://127.0.0.1:8000/specialty/<specialty_name-number_of_sort>/
```
- Create a new doctor or specialty
``` 
http://127.0.0.1:8000/doctors/create/
http://127.0.0.1:8000/specialties/create/
```