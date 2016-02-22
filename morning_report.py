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
import email_drafting_utils
import logging

# Establish global variables from config file
key = config.wunderground_key
local_zip = config.local_zip
dev_email = config.dev_email
dev_email_password = config.dev_email_password
recipient_email = config.recipient_email

# Get today's forecast
forecast = weatherservice_utils.get_todayforecast(key, local_zip)

conditions = forecast[0]
high = forecast[1]
low = forecast[2]

message_to_email = email_drafting_utils.write_morning_email(conditions, high, low)
print message_to_email

email_utils.send_email(dev_email, dev_email_password, recipient_email, message_to_email)