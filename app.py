monthConversions = { #Dictionaries- key: value pair, keys can't be repeated
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
    }

print(monthConversions["Sep"])
#print(monthConversions["August"]) #Error no key "August"
print(monthConversions.get("August", "Not a valid key"))     #Can assign defaults if key not found
