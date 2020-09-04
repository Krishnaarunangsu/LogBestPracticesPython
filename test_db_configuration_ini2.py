import configparser


# Instantiate ConfigParser
config = configparser.ConfigParser()

# Read Configurations from INI file
config.read("resources/config.ini")

print(config['db']['default_username'])
