# write the code that transforms a string to a list
# where the elements of the list are separated by 
# a pattern you have to recognize


# HINT: use the split() function
a = "11|12|78"
b = a.split("|")
print(b)

b = "11*|*22*|*8"
# should print: ['11', '22', '8']


c = """11
22
33"""
# should print: ['11', '22', '8']
