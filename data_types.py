#BUILT-IN DATATYPES:
#1. Text Type: string
# string1="Hello my dear coder girls!"
# print(type(string1))           #<class 'str'>

# #2. Numeric Types:
# #a. Integer:
# a=10
# print(type(a))   #<class 'int'>

# #b. Float:
# b=10.0
# print(type(b))   #<class 'float'>

# #c. Complex:
# c=2+6j
# print(type(c))   #<class 'complex'>
 

#3. Sequence types:
#a. List:
# d=["apple","banana","grapes"]
# print(type(d))   #<class 'list'>

#b. Tuple:
# e=("apple","banana","grapes")
# print(type(e))   #<class 'tuple'>

#c. Range:
# f=range(6)
# print(f)      #range(0, 6)
# print(type(f))  #<class 'range'>

#4. Mapping types: Dictionary:
# g={"name":"Isa",
#    "age":22,
#    }
# print(g)     #{'name': 'Isa', 'age': 22}
# print(type(g))   #<class 'dict'>

#5. Set Types:
#a. set:
# h={"apple","mango","banana"}
# print(h)    #{'apple', 'banana', 'mango'}
# print(type(h))      #<class 'set'>

#b. frozenset:
# i=frozenset({"apple","banana","cherry"})
# print(i)   #frozenset({'apple', 'banana', 'cherry'})
# print(type(i))   #<class 'frozenset'>

# #6. Boolean Type:
# j=True
# print(j)  #True
# print(type(j))  #<class 'bool'>

#7. Binary Types:
#a. Bytes:
# k=b"Hello"
# print(k)   #b'Hello'
# print(type(k))   #<class 'bytes'>

#b. Bytearray:
# l=bytearray(6)
# print(l)   #bytearray(b'\x00\x00\x00\x00\x00\x00')
# print(type(l))   #<class 'bytearray'>

#c.Memoryview:
m=memoryview(bytes(6))   
print(m)   #<memory at 0x0000020BECFA4AC0>
print(type(m))  #<class 'memoryview'>

#8. None:
n=None
print(n)  #None
print(type(n))   #<class 'NoneType'>