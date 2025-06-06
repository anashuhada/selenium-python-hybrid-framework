import os
from configparser import ConfigParser

def read_configuration(category, key):
    config = ConfigParser()
    base_dir = os.path.dirname(os.path.dirname(__file__))  # Go to project root
    config_path = os.path.join(base_dir, 'configurations', 'config.ini')
    config.read(config_path)
    return config.get(category, key)
