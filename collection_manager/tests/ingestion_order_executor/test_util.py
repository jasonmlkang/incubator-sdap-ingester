import logging
import os
import unittest

from collection_manager.config import LocalConfiguration
from collection_manager.collection_manager.util import ConfigWithPath

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class MyTestCase(unittest.TestCase):
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               '..', '..',
                               'resources', 'config')

    def test_read_local_configuration(self):
        config = LocalConfiguration(config_path=self.config_path).get()
        logger.info(f"interpolated value is {config['COLLECTIONS_YAML_CONFIG']['yaml_file']}")

    def test_config_with_path(self):
        config_with_path = ConfigWithPath()
        config_with_path.read([os.path.join(self.config_path, 'collection_manager.ini.default')])
        logger.info(config_with_path.get('INGESTION_ORDER_YAML_CONFIG', 'yaml_file'))
        logger.info(config_with_path.get('GIT_CONFIG', 'git_local_dir'))


if __name__ == '__main__':
    unittest.main()