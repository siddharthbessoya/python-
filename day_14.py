import datetime


# Import the datetime module and display the current date

x = datetime.datetime.now()
print(x)


# When we execute the code from the example above the result will be: 2022-05-15 17:38:34.858080
# The date contains year, month, day, hour, minute, second, and microsecond.
# The datetime module has many methods to return information about the date object.


# Return the year from the datetime object:
print(x.year)


# Return the month from the datetime object
print(x.month)


# Return the day from the datetime object
print(x.day)


# Return the hour from the datetime object
print(x.hour)


# Return the minute from the datetime object
print(x.minute)


# Return the second from the datetime object
print(x.second)


# Return the name of weekday:
print(x.strftime('%A'))

# Directive	Description	                Example
# %a	    Weekday,    short version	Wed	
# %A	    Weekday,    full version	Wednesday
# %w	    Weekday as a number 0-6, 0 is Sunday	3	
# %d	    Day of month 01-31	        31	
# %b	    Month name, short version	Dec	
# %B	    Month name, full version	December	
# %m	    Month as a number   01-12	12	
# %y	    Year, short version, without century	18	
# %Y	    Year, full version	        2018	
# %H	    Hour 00-23	                17	
# %I	    Hour 00-12	                05	
# %p	    AM/PM	PM	
# %M	    Minute 00-59	            41	
# %S	    Second 00-59	            08	
# %f	    Microsecond 000000-999999	548513	
# %z	    UTC offset	                +0100	
# %Z	    Timezone	                CST	
# %j	    Day number of year          001-366	365	
# %U	    Week number of year, Sunday as the first day of week, 00-53	52	
# %W	    Week number of year, Monday as the first day of week, 00-53	52	
# %c	    Local version of date and time	Mon Dec 31 17:41:00 2018	
# %C	    Century	                    20	
# %x	    Local version of date	    12/31/18	
# %X	    Local version of time	    17:41:00	
# % %	    A % character	            %	
# %G	    ISO 8601 year	            2018	
# %u	    ISO 8601 weekday            (1-7)	1	
# %V	    ISO 8601 weeknumber            (01-53)	01	



# Construct a date using datetime 
y = datetime.date(2022, 5, 15)
print(y)
