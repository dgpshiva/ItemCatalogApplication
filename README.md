# Item Catalog Application

This repository contains code to host an Item Catalog web application. The Item Catalog application can be used to maintain a catalog of different vehicle types and their details. Non-logged in users will have a read only view of the application. They can view all the different categories and items within each category. A user can log into the application using their google account. Once logged in they can create their own categories and items or even add their own items to categories created by other users.


## Table of content
- [Requirements to run the code](#requirements-to-run-the-code)
- [Running the code](#running-the-code)
- [Navigating the application](#navigating-the-application)
- [Stopping the code](#stopping-the-code)
- [Known issues](#known-issues)
- [References](#references)


## Requirements to run the code
- Python (version 2.7 or higher is preferred) needs to be installed on the machine where the code will be run
- The following python libraries need to be installed if not already present: flask, httplib2, json, oauth2client, random, requests, sqlalchemy, string, flask_httpauth
- sqlite3 needs to be installed on the machine where the code will be run

## Running the code
### To run the application on local machine:
- Pull the code from branch 'release-v1' of this repository
- Navigate to the folder /ItemCatalogApplication using terminal (for Mac) or command prompt (for Windows)
- Run the python code [database_setup.py](./database_setup.py) using the command `python database_setup.py`
- This should create a file named "transportitemswithusers.db" in the same folder as [database_setup.py](./database_setup.py)
- Run the python code [application.py](./application.py) using the command `python application.py`
- Leave the terminal/command prompt window open
- Open your preferred internet browser and navigate to 'localhost:8000'
- This should open up the Item Catalog Application

### To run the application on vagrant machine:
- Download and install Vagrant for [Windows](https://releases.hashicorp.com/vagrant/2.1.1/vagrant_2.1.1_x86_64.msi) or [Mac](https://releases.hashicorp.com/vagrant/2.1.1/vagrant_2.1.1_x86_64.dmg)
- Download and install Virtual Box for [Windows](https://download.virtualbox.org/virtualbox/5.1.36/VirtualBox-5.1.36-122416-Win.exe) or [Mac](https://download.virtualbox.org/virtualbox/5.1.36/VirtualBox-5.1.36-122089-OSX.dmg)
- Pull the code from 'release-v1' branch of this repository
- Open the file [application.py](./application.py) under /ItemCatalogApplication folder
- Comment out the last line `app.run(host='127.0.0.1', port=8000)`
- Uncomment the line `app.run(host='0.0.0.0', port=8000)`
- Navigate to the folder /ItemCatalogApplication using terminal (for Mac) or command prompt (for Windows)
- Run the command `vagrant up` to start the vagrant machine
- Log into the vagrant machine using the command `vagrant ssh`
- Change to vagrant directory using `cd /vagrant` command
- Run the python code [database_setup.py](./database_setup.py) using the command `python database_setup.py`
- This should create a file named "transportitemswithusers.db" in the same folder as [database_setup.py](./database_setup.py)
- Run the python code [application.py](./application.py) using the command `python application.py`
- Leave the terminal/command prompt window open
- Open your preferred internet browser and navigate to 'localhost:8000'
- This show open up the Item Catalog Application


## Navigating the application:
- You need a Google account to log into this application. Create one if you do not already have one by visiting [Create your Google Account](https://accounts.google.com/signup)
- Click the green _Login_ button on top right to log into the application using your google account
- Click on _Add New Category_ green button
- Enter a new category name to create a new category
- Click on the new category tile
- Click on _Edit Category_ blue button to edit the category or _Delete Category_ red button to delete this category
- Click on _Add New Item_ green buttton
- Enter item details to create a new item within this category
- Click on the new item tile. This will display the item's details and info about the item's creator
- Click on _Edit Item_ blue button to edit this item or _Delete Item_ red button to delete this item
- Click on the red _Logout_ button on top right to log out of the application
- In logged-out mode you will not be able to add/edit/delete categories or items but you will still be able to browse them
- Click on the _Latest Items_ tile to view the last 5 items that have been created by users
- **_Tip_**: Click on "Catalog App" header in any page to navigate back to the Categories home page


## Stopping the code
### If application was run on local machine:
- Close the Item Catalog application website if open
- Press Ctrl+C on the open terminal/command propmt window
- Close the terminal/command prompt window

### If application was run on vagrant machine:
- Close the Item Catalog application website if open
- Press Ctrl+C on the open terminal/command propmt window
- Exit the vagrant machine using the command `exit`
- Run the command `vagrant halt` to stop the vagrant machine
- Close the open terminal/command prompt window


## Known issues
- On a mac, trying to run the app again (after having stopped it) using the command `python application.py` may throw an error that the port 8000 is already in use
- Run the following command `sudo lsof -i tcp:8000` on terminal window to find the ids of the processes running on this port
- Find the ids of python processes from the output of the above command
- Run the command `kill -9 <process id>` to kill the python processes
- Now run the command `python application.py` again and the app should launch succesfully


## References
- The website design has been inspired from [Api List](https://apilist.fun/). References have been taken from their [css styling page](https://apilist.fun/stylesheets/style.css)
