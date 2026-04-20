
import re
text = "My telephone number is 408-555-1234"

phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)

re.search(r'\d{3}-\d{3}-\d{4}',text)
#Groups
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)
# The entire result
results.group()
# Can then also call by group position.
# remember groups were separated by parentheses ()
# Something to note is that group ordering starts at 1. Passing in 0 returns everything
results.group(1)
#Or operator |
re.search(r"man|woman","This man was here.")

#The Wildcard Character
"""
Use a "wildcard" as a placement that will match any character placed there.
You can use a simple period **.** for this. For example:
"""
re.findall(r".at","The cat in the hat sat here.")

re.findall(r".at","The bat went splat")

re.findall(r"...at","The bat went splat")
#Starts With and Ends With
#We can use the ^ to signal starts with, and the $ to signal ends with:
#End with
re.findall(r'\d$','This ends with a number 2')
# Starts with a number
re.findall(r'^\d','1 is the loneliest number.')
