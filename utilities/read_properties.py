import configparser
import os
from pathlib import Path


class Properties:

    config = None

    def __init__(self):
        path = Path(__file__)
        root_dir = path.parent.absolute()
        config_path = os.path.join(root_dir, 'Configurations/config.ini')
        global config
        config = configparser.ConfigParser()
        config.read(config_path)

    @staticmethod
    def get_property(key):
        return config.get('common', key)
