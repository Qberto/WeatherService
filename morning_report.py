#-------------------------------------------------------------------------------
# Name:        morning_report.py
# Purpose:     Driver for morning report 
#              
#
# Author:      Alberto
#
# Created:     21/02/2016
# Copyright:   (c) Alberto 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import config
import weatherservice_utils
import email_utils
import logging

# Establish global variables from config file
key = config.wunderground_key
local_zip = config.local_zip
dev_email = config.dev_email
dev_email_password = config.dev_email_password
message_greeting = config.message_greeting

# Get today's forecast
forecast = weatherservice_utils.get_todayforecast(key, local_zip)

conditions = forecast[0]
high = forecast[1]
low = forecast[2]

def write_morning_email(message_greeting, conditions, high, low):
	import config

	# Start message with the greeting
	message = config.message_greeting
	message += "\n"

	# Create conditional logic
	if conditions in config.rain_conditions_text:
		message += "Better take your umbrella little love! Today's conditions are: {0}".format()