import configparser

config = configparser.ConfigParser()

config.read('config.ini')

for key in config['default']:
    # print(config['default'][key])
    host = config['default']['host']
    username = config['default']['username']
    password = config['default']['password']
    db_fan = config['default']['db_fan']
    api_key = config['default']['api_key']



print(host, username, password, db_fan, api_key)