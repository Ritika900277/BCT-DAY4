s={}
print(type(s))

p={1,4,2,5}
print(type(p))

a={1,2,5,3}
print(a)

b={1,2,3,4}
b.add(5)
print(b)

e={1,2,3}
f={1,3,5,7}
e.update(f)
print(e)

q={1,2,4,3,6}
q.discard(4)
print(q)
q.remove(4)
print(q)