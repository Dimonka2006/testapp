d1 = {"foo": "bar", "bar": "foo"}
d2 = {"key": "values"}
d3 = {}
for i in d1:
    print(i)
    print(d1[i])
    d3[i] = d1[i]

for p in d2:
    print(p)
    print(d2[p])
    d3[p] = d2[p]

print(d3)
    
