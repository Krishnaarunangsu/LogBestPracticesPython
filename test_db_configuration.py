from typing import List , Any , Union , TextIO
import yaml

db_configuration: TextIO

# Load the Configuration file
with open('resources/config.yml', 'r') as db_configuration:
    doc = yaml.load(db_configuration)

db_name: Union[List[Any], Any] = doc["DB_NAME"]
db_host=doc["DB_HOST"]
db_user: Union[List[Any], Any]=doc["DB_USER"]
db_password=doc["DB_USER_PASSWORD"]
db_port: Union[List[Any], Any]=doc["DB_PORT"]

#**********Printing*************
print("Databased name: {}".format(db_name))
print("Database Host/url: {}".format(db_host))
print("Database User: {}".format(db_user))
print("Database password: {}".format(db_password))
print("Database Port: {}".format(db_port))
print('********************************************************')
print("Database Configuration Details: {}".format(doc))
