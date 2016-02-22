#-------------------------------------------------------------------------------
# Name:        draft_morning_email.py
# Purpose:     email writing utility 
#              
#
# Author:      Alberto
#
# Created:     21/02/2016
# Copyright:   (c) Alberto 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def write_morning_email(message_greeting, conditions, high, low):
	import config

	# Start message with the greeting
	message = config.message_greeting
	message += "\n"
	message += "You might already know but just in case...\n"

	# Create weather conditional logic
	if conditions in config.rain_conditions_text:
		message += "Better take your umbrella little love! Today's conditions are: {0}\n".format(conditions)
		message += "Please be careful driving my sweet love."
	elif conditions in config.snow_conditions_text:
		message += "Please bundle up! Today's conditions are: {0}\n".format(conditions)
		message += "Please be careful driving my sweet love."

	message += "The high today will be {0}\n".format(high)
	message += "The low today will be {1}\n".format(low)

	message += "\nPlease don't forget that I love you with all my heart no matter what."
	message += "\nHave an amazing day!"
	message += "\n Love always and forever,\nBerto"

	return message