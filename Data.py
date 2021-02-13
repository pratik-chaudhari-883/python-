import sys
x=11
print(x)   # 11 

print(type(x)) # <class 'int'> 

print(id(x)) # it is use to display unique id of the object (Address)

x=12 
print(x)
print(type(x))
print(id(x))



a=12 
print(a)
print(type(a))
print(id(a))


b=12.5
print(b)
print(type(b))
print(id(b))

c=12+3j
print(c)
print(type(c))
print(id(c))


d="Hello"
print(d)
print(type(d))
print(id(d))


e= True
print(e)
print(type(e))

f=[10,20,30,40]
print(f)
print(type(f))

g={10,20,30,40}
print(g)
print(type(g))

h=(10,20,30,40)
print(h)
print(type(h))

i={"a":10,"b":20,"c":30,"d":40}
print(i)
print(type(i))

k= None
print(k)
print(type(k))

l=11
print(l)
print(type(l))
print(sys.getsizeof(l))


m=11**123
print(m)
print(type(m))
print(sys.getsizeof(m))

