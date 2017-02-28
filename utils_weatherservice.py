#-------------------------------------------------------------------------------
# Name:        Weather Services
# Purpose:     Functions that assist in getting weather reports from weather 
#              underground's API
#
# Author:      Alberto
#
# Created:     21/02/2016
# Copyright:   (c) Alberto 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def get_current_weather(key, zip):
    # Import needed modules
    try:
        # For Python 3.0 and later
        from urllib.request import urlopen
    except ImportError:
        # Fall back to Python 2's urllib2
        from urllib2 import urlopen
    import json
    # Create request url
    url = 'http://api.wunderground.com/api/{0}/geolookup/conditions/q/PA/{1}.json'.format(key, zip)
    # Open the request url
    f = urlopen(url)
    # Read the response and load into a json
    json_string = f.read().decode('utf-8')
    parsed_json = json.loads(json_string)

    # Parse response json content
    city = parsed_json['location']['city']
    state = parsed_json['location']['state']
    weather = parsed_json['current_observation']['weather']
    temperature_string = parsed_json['current_observation']['temperature_string']
    feelslike_string = parsed_json['current_observation']['feelslike_string']

    # Create result and close the response file
    print('Weather in {0}, {1}: {2}. The actual temperature is {3} and it feels like {4}.'.format(city, state, weather.lower(), temperature_string, feelslike_string))
    f.close()
    return weather, temperature_string, feelslike_string

    #TODO - Change function so that result is returned rather than printed

def print_tendayforecast(key, zip):
    try:
        # For Python 3.0 and later
        from urllib.request import urlopen
    except ImportError:
        # Fall back to Python 2's urllib2
        from urllib2 import urlopen
    import json
    url = 'http://api.wunderground.com/api/{0}/geolookup/forecast10day/q/{1}.json'.format(key, zip)
    f = urlopen(url)
    json_string = f.read().decode('utf-8')
    parsed_json = json.loads(json_string)
    for day in parsed_json['forecast']['simpleforecast']['forecastday']:
        print("{0} ({1}):".format(day['date']['weekday'], day['date']['pretty']))
        print("    Conditions: {0}".format(day['conditions']))
        print("    High: {0}F".format(day['high']['fahrenheit']))
        print("    Low: {0}F".format(day['low']['fahrenheit']))
    f.close()

def get_todayforecast(key, zip):
    try:
        # For Python 3.0 and later
        from urllib.request import urlopen
    except ImportError:
        # Fall back to Python 2's urllib2
        from urllib2 import urlopen
    import json
    url = 'http://api.wunderground.com/api/{0}/geolookup/forecast10day/q/{1}.json'.format(key, zip)
    f = urlopen(url)
    json_string = f.read().decode('utf-8')
    parsed_json = json.loads(json_string)
    for day in parsed_json['forecast']['simpleforecast']['forecastday']:
        conditions = day['conditions']
        high = day['high']['fahrenheit']
        low = day['low']['fahrenheit']
        break
    return conditions, high, low

if __name__ == '__main__':
    key = '0a3a7926e3b32d4f'
    zip = input('For which ZIP code would you like to see the weather? ')
    mode = input("Would you like a current weather report or a forecast? (current/forecast)")
    if mode == "current":
        get_current_weather(key, zip)
    elif mode == "forecast":
        get_todayforecast(key, zip)