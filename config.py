import os, json

# get json data
if os.environ['APP_SETTINGS'] == "config.DevelopmentConfig":
    jsonfile2 = 'api_info.json'
else:
    jsonfile2 = 'api_info_blank.json'

with open(jsonfile2, 'r') as myfile:
    data2=myfile.read()
apiData = json.loads(data2)

class BaseConfig(object):
    DEBUG = False
##################################################################
    SECRET_KEY = apiData["api_data"]["app_secret_key"]["secret_key"]


###################################################################

class ProductionConfig(BaseConfig):
    DEBUG = False
    ENV = 'production'
    ##### dc
    WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    ENV = 'development'
    #### test data
    WEATHER_API_KEY = apiData["api_data"]["weather"]["client_key"]
    # GOOGLE_API_Key = apiData["api_data"]["google"]["api_key"]
