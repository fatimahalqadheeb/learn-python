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
