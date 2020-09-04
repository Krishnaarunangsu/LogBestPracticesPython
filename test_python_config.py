# Importing configurations from config.py
import config


username=config.config['username']
password = config.config['password']
print("Username: {}".format(username))
print("Password: {}".format(password))
