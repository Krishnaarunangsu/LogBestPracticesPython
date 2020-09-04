from typing import Dict , List , Any , Union , Hashable
import yaml


config: Union[Union[Dict[Hashable, Any], List[Any], None], Any] = yaml.load(open('resources/config.yml'))
# print(config.DB_NAME)  # will Give Error
db_name = config['DB_NAME']
db_user_name = config['DB_USER']
db_user_password: Union[List[Any], Any] = config['DB_USER_PASSWORD']
db_url = config['DB_HOST']
print('Database name: {}'.format(db_name))
print('Database user: {}'.format(db_user_name))
print('Database password: {}'.format(db_user_password))
print('Database url: {}'.format(db_url))

db_config =  {
            'host': db_url,                 # database host
            'port': 3306,                       # port
            'user': db_user_name,                      # username
            'password': db_user_password,                   # password
            'db': db_name,                        # database
            'charset':'utf8'                    # charset encoding
            }
