#-------------------------------------------------------------------------------
# Name:        E-mail Utilities
# Purpose:
#
# Author:      Alberto
#
# Created:     21/02/2016
# Copyright:   (c) Alberto 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def send_email(account, password, recipient_email, message):
	
	# Import needed modules
	import smtplib
	
	# Create an smtplib object - used as a sort of portal through which we access our
	# connection and the various capabilities provided by the smtplib package for 
	# doing things with tat connection. 
	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

	# Tell the SMTP object that we need to encrypt our message
	smtpObj.starttls()

	# Login to the account
	smtpObj.login(account, password)

	# Send the e-mail
	smtpObj.sendmail(account, recipient_email, message)

	# Close smtp connection
	smtpObj.quit()

if __name__ == "__main__":
	
	# Import needed modules
	import getpass
	
	# Ask the user for the account, password, recipient email, and message
	account = raw_input("Your e-mail address: ")
	password = getpass.getpass()
	recipient_email = raw_input("Recipient e-mail address: ")
	message = raw_input("Message: ")

	# Invoke the send_email function to send the designated message
	print("Sending your message...")
	send_email(account, password, recipient_email, message)
	print("Message sent.")