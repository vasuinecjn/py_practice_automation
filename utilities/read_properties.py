import configparser

config = configparser.RawConfigParser()
config.read('../Configurations/config.ini')


class Properties:
    @staticmethod
    def get_property(key):
        return config.get('common info', key)
