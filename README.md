# blockhouseOADjango
A simple Django server that serves data to blockhouseOANextJS

# Steps to run the project
1) python3 manage.py runserver

This should start the server on [This Link](http://127.0.0.1:8000)

NOTE: Need to run server before UI, as UI needs data from the server.

# Thoughtprocess
1) Created 4 different endpoints which serves data from static files as mentioned in the problem statement.
2) These files can later be replaced with DB queries
3) Reduced code redundancy by genralising the common functions.