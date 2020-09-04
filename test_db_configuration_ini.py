#Importing the modules
import os
import configparser
import time


# Instantiate ConfigParser
config = configparser.ConfigParser()

# Read Configurations from INI file
config.read("config.ini")
user_name = config.get('db', 'username')
password = config.get('db', 'password')
# hostname = config.get('db', 'host')
file_stamp = time.strftime('%Y-%m-%d')

#***********************Print***********************************
print("User Name: {}".format(user_name))
print("Password: {}".format(password))
print("Time: {}".format(file_stamp))
