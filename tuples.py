t = 12345, 54321, 'hello!'
t[0]

t

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)

# Tuples are immutable:
L = list(t)
L[0] = 88888
print(L)




# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v
