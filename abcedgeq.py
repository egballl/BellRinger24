e = int(input("Shift ")) 
x = 'Baez Knows!'
s = ''.join((chr(ord(_) + e) for _ in x))
print(s)
