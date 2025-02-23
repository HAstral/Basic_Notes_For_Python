x={1,2,4,5,6}
print(x)
y={"hi","mm","hee"}
print(y)
y.add("ahhh")
print(y)
y.remove("mm")#will error when the key is not available
y.discard("mm")#will not get error
print(y)
z=set()
print(type(z))
# x.pop()#randomly delete
# print(x)
# del(x) #all delete    
a={9,4,6}
b={2,3,4}
# c=a.difference(b)
c=a.intersection(b)
print(c)
print(x.isdisjoint(y))#false if x interset y 

