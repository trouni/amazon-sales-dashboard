#!/usr/bin/python
from configparser import ConfigParser


def config(filename='dashboard.cfg', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    configdata = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            configdata[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} not found in the {1} file'.format(section, filename))
    return configdata


print(config())
