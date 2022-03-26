from configparser import ConfigParser
import os

class Configuration:

    @staticmethod
    def config(filename, section):   # filename='database.ini', section='postgresql'):
        # create a parser
        parser = ConfigParser()
        # read config file
        result = parser.read(filename)

        # get section
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        return db
