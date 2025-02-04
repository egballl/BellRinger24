e = int(input("Shift ")) 
x = 'Baez Knows!'
s = ''.join((chr(((ord(_) - 65 + e) % 26) + 65) if _.isupper() else chr(((ord(_) - 97 + e) % 26) + 97) if _.islower() else _ for _ in x))
print(s)
