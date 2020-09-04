import os

from configparser import ConfigParser

parser = ConfigParser()
parser.read('database.conf')

# print(parser.get('database_config', 'url'))
db_url = parser.get('database_config', 'url')
print(db_url)
# if os.environ['COMPUTERNAME'] == 'WIN-E39OLKT8K4F':
# print(parser.get('UK_PDL', 'db.user_name'))
