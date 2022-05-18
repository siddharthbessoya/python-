import re

# RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.
# Python has a built-in package called re, which can be used to work with Regular Expressions.


# The re module offers a set of functions that allows us to search a string for a match:

# Function	    Description
# findall	    Returns a list containing all matches
# search	    Returns a Match object if there is a match anywhere in the string
# split	        Returns a list where the string has been split at each match
# sub	        Replaces one or many matches with a string




txt = 'He passed in IELTS Exam'

x = re.search('^He.*Exam$', txt)
if x:
    print('We have a match!')
else:
    print('No match...')



# Character	Description	                    Example	
# []	    A set of characters	            "[a-m]"
# \	        Signals a special sequence (can also be used to escape special characters)	"\d"
# .	        Any character (except newline character)	"he..o"
# ^	        Starts with	                    "^hello"
# $	        Ends with	                    "planet$"
# *	        Zero or more occurrences	    "he.*o"
# +	        One or more occurrences	        "he.+o"
# ?	        Zero or one occurrences	        "he.?o"
# {}	    Exactly the specified number of occurrences	"he.{2}o"
# |	        Either or	                    "falls|stays"



