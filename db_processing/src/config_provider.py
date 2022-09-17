""" Utility class to convert YAML file to a DICTIONARY """

import yaml


class ConfigurationProvider:
    """
    Create a configuration based on a config file
    """

    def __init__(self, config={}):
        self.config = config

    def configure(self, config_path: str):
        """
        Pull configurations from config/<file>.yml file
        into a dictionary object names ``self.config``

        Parameters
        ----------
            config_path : str
                Path to the location of the config file

        Returns
        -------
            config : dict
                A dictionary of the configuration keys and values
        """

        with open(config_path, encoding="utf-8") as file:
            config = yaml.load(file, Loader=yaml.FullLoader)

        return config