# write the code that transforms a string to a list
# where the elements of the list are separated by 
# a pattern you have to recognize


# HINT: use the split() function
a = "11|12|78"
b = a.split("|")
print(b)

a = "11*|*22*|*8"
# should print: ['11', '22', '8']


a = "11, 22, 8" 
# should print: ['11', '22', '8']
