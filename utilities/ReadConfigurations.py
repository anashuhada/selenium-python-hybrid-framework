import os
from configparser import ConfigParser


def read_configuration(category, key):
    config = ConfigParser()
    config_path = "../configurations/config.ini"

    # Debug prints
    # print("Looking for config file at:", os.path.abspath(config_path))
    # print("File exists:", os.path.exists(config_path))

    config.read(config_path)
    return config.get(category, key)
