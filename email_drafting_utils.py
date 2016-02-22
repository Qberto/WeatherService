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

def write_morning_email(conditions, high, low):
	import config

	# Start message with the greeting
	message = config.message_greeting
	message += "\n"
	message += "You might already know about the weather today but just in case...\n\n"

	# Create weather conditional logic
	if conditions in config.rain_conditions_text:
		message += "\tBetter take your umbrella little love! Today's conditions are: {0}\n".format(conditions)
		message += "\tPlease be careful driving my sweet love."
	elif conditions in config.snow_conditions_text:
		message += "\tPlease bundle up! Today's conditions are: {0}\n".format(conditions)
		message += "\tPlease be careful driving my sweet love."
	else:
		message += "\tToday's conditions are: {0}\n".format(conditions)

	message += "\tThe high today will be {0}\n".format(high)
	message += "\tThe low today will be {0}\n".format(low)

	message += "\nPlease don't forget that I love you with all my heart no matter what."
	message += "\nHave an amazing day!"
	message += "\n\nLove always and forever,\nBerto"
	message += "\n\nPS: If you want me to stop sending you these emails... :(\n... just reply with the message: 'MAD MAX FURY ROAD WAS THE BEST MOVIE OF 2015'... :) "

	return message