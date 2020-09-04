import logging
import logging.config
import yaml

# with open("path/to/yaml", 'r') as the_file:
with open("resources/logging.yml", 'r') as the_file:
    config_dict = yaml.load(the_file)

logging.config.dictConfig(config_dict)

logger = logging.getLogger(__name__)
logger.debug('Abzooba-AI Analytics')
logger.warning('Age of AI')
