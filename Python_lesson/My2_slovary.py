#переменные и словари

d = {"house":"House in Moscow","money":"gold"}
print (d)

d1 = dict (h1="House in Moscow", g2="key in garden")
print (d1)

d2 = dict.fromkeys ( ['a1', 'a2'] )
d2["a1"] = 10
print (d2)

d3 = {a: a**2 for a in range (1, 8)}
print (d3)

d2.clear
print (d2)

d2 = d3
d2 ["keynew"] = "This is new key!"
print (d2)

d2 = d3.copy ()
d3.pop("keynew")
print (d3)

d3.keys ()
d2.keys ()

print (d2, d3)

d3 [3] = 99
print (d3)

d2.update (d3)
print (d2)

d3 ["33"] = "333333"
d2.update (d3)
print (d2)
d3.values()
 











