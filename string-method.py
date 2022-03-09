print("hello python")
print("hello myself")
# --------------------------
# hello this is  multiple comments
# --------------------------
myString = "I love Python"
print(myString[3:5])  # start include but end not include
print(myString[8:11])
print(myString[8:])  # will print from index 8 to the end (ython)

fname = "fatimah mohammed alqadheeb"
print(fname.title())  # each world will be capital
print(fname.capitalize())  # only firat word will be cabital

a, b, c, = "1", "11", "111"

print(a.zfill(3))
print(b.zfill(3))
print(c.zfill(3))

d = "fatimah"
print(d.center(15))  # make the string in the center with space
print(d.center(15, "@"))

e = "I love Python and PHP"
print(e.count("PHP"))  # how many times appeared
print(e.count("PHP", 0, 5))  # count in a length of text start:end

f = "I love Python and PHP"
print(f.split())  # divide the strings

g = "      I love Python and PHP        "
print(g.strip())  # remove spacce from end and stsrt rsplit/ lstrip
print(g.rstrip())
print(g.lstrip())

g = "######I love Python and PHP#####"
print(g.strip("#"))  # remove charchter
print(g.rstrip("#"))
print(g.lstrip("#"))

h = "I love python"
print(h.startswith("I"))  # check id string start with a letter, boolean result
print(h.startswith("P"))
print(h.startswith("p", 7, 12))
print(h.endswith("n"))  # check the end of the string

# index(subString, start, end) find the index of an elements
# find(subString, start, end) does not through error when item not found ir results with -1
i = "fatimah"
print(i.index("f"))

# rjust(width, symbol) ljust() fill the space with symbol

j = "fatimah"
print(j.rjust(15, "#"))
print(j.ljust(15, "#"))

# splitlines() return a list of lines
k = """first line
second line
third line
"""
print(k.splitlines())

# replace(oldVlue, new value, count)
l = "one two three one one"
print(l.replace("one", "1"))
print(l.replace("one", "1", 2))

# join(Iterable)
m = ["fatimah", "mohammed", "alqadheeb"]  # list
n = {"fatimah", "mohammed", "alqadheeb"}  # set
print(" ".join(m))
print("-".join(m))
print(", ".join(m))
print(type(", ".join(m)))  # it will be a string
