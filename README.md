# Engineering Project
This is a project that we use for testing potential team members on their technical skills.

## Feature Request App
Build a web application that allows the user to create "feature requests".

A "feature request" is a request for a new feature that will be added onto an existing piece of
software. Assume that the user is an employee at IWS who would be entering this information after
having some correspondence with the client that is requesting the feature.  The necessary fields
are:

* **Title:** A short, descriptive name of the feature request.
* **Description:** A long description of the feature request.
* **Client:** A selection list of clients (use "Client A", "Client B", "Client C")
* **Client Priority:** A numbered priority according to the client (1...n). Client Priority numbers
should not repeat for the given client, so if a priority is set on a new feature as "1", then all
other feature requests for that client should be reordered.
* **Target Date:** The date that the client is hoping to have the feature.
* **Product Area:** A selection list of product areas (use 'Policies', 'Billing', 'Claims',
'Reports')

## Tech Stack Requirements
The following are requirements on the tech stack. This stack demonstrates mastery of tools our team favors.

* OS: Ubuntu
* Server Side Scripting: Python 2.7+ or 3.5+
* Server Framework: Flask or SimpleHTTPServer
* ORM: Sql-Alchemy
* JavaScript: KnockoutJS

Make sure that your instructions for accessing or otherwise running your code are extremely clear.

## Running the project with `` docker-compose up ``

If you have docker-compose installed on your ubuntu machine, the project runs with a single command i.e `` docker-compose up ``

--

## Running the project in windows machine
- Install python
- Install mysql
- Install requirements using pip install -r requirementx.txt
- Create database engineering
- Change the hostname in database string at settings.py to localhost
- run the project using python runserver.py

## Visit Live Project

The project is hosted live at http://ec2-54-234-232-117.compute-1.amazonaws.com:5001


## TECHNOLOGY AND ARCHITECTURE

1. *Open Source:* uses python, flask, sqlalchemy as orm, mysql as database

2. *Decoupled Backend: * There are following modules in the system:
- urls.py: servers as router, contains api endpoint configuration
- models.py: contains model for table definition on top of mysql database
- manager.py: manager class for all the models in models, handles logical aspect of crud opretaion
- settings.py: contains configuration details
- views.py: logical aspect of url routing 
- testfiles.py: contains all the testcases for api end points
- static fodler: contains all the static files
- templates: contains templates

3. *Test Suites with Continuous Integration*. all the unit test for api end points are kept inside testfiles.

4. *Automated Deployment*. Automated deployment to AWS using Jenkins has been configured at:
http://ec2-54-234-232-117.compute-1.amazonaws.com:8080/

5. *Usable, Responsive Interface*. For responsive UI, bootstrap has been used. Datatable has been used for listing feature request.

6. *MVVM Frontend*. Projects uses Knockout.js.

--

Thank you for your time.