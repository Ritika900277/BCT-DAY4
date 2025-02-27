a={1,2,3,5,8}
b={2,3,4,6,7}
c=a.intersection(b)
print(c)
d=a.union(b)
print(d)

e={1,2,3,4}
f={2,3}
g=f.issubset(e)
print(g)
h=f.issuperset(e)
print(h)

j={3,4,2,5}
h=j.pop()
print(h)
