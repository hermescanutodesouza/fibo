# Introduction 
A robot that applies one of the fibonacci sequences to indicate the moment of purchase or sale.

# Getting Started

1.	Installation process
2.	Software dependencies
3.  Run the ROBOT


### Instalation Process

1) Python 3.6 or greater
2) Clone the project 
3) Edit the file **database/config** and configure credential for database access
   ```
     autotrade = {
        "user": "????",
        "password": "????",
        "host": "????",
        "database": "????",
    }
   
    ordem = {
        "user": "????",
        "password": "????",
        "host": "????",
        "database":"????"
     }
    ```
    


### Software dependencies

   
 1) All dependencies are defined in the file **requirements.txt** ,Located at the root of the project.
 2) To install all the dependencies
 ```
     pip install -r requirements.txt
 ```


### Run the project
 ```
    python all.py
 ```