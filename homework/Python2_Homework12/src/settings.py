"""
Config file for JOTD sender
"""
import datetime

# Send JOTD email to these people
RECIPIENTS = [("Fred", "fred@example.com"), ("Barney", "barney@example.com"),
              ("Wilma", "wilma@example.com"), ("Betty", "betty@example.com")]

# start sending emails on this date
#  Format must be 'YYYY-MM-DD'
DATE = '2013-11-08'
STARTTIME = datetime.datetime.strptime(DATE, '%Y-%m-%d')

# send the emails once a day for this number of days
DAYCOUNT = 5