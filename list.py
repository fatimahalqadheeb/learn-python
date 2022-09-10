colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'white']
print(type(colors))

colors.append('pink')
print(colors)

colors.insert(1, 'black')
print(colors)

colors.remove('pink')
print(colors)

colors.clear()
print(colors)

colors.append('pink')
print(colors)

colors[0] = 'green'
print(colors)
