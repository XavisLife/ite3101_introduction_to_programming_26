# It is hard-coded but not sure if we could import the datetime library for this task..
# We could use datetime.datetime.now():%d/%m/%Y to present the up-to-date current date.
# todays_date = "08/09/2026"

from datetime import datetime
now = datetime.now()
todays_date = "%02d/%02d/%04d" % (now.day, now.month, now.year)
