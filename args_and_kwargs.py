#1. *args:
# def funargs(*args): 
#     print(args)   #('hello', 'dear', 'coders')
#     print(args[0])   #hello
# har=("hello","dear","coders")
# funargs(*har)

#2. The name can be anything else as well:
# def funargs(*isa): 
#     print(isa)   #('hello', 'dear', 'coders')
#     print(isa[0])   #hello
# har=("hello","dear","coders")
# funargs(*har)


# def funargs(*args):
#     for x in args:
#         print(x)

# har=("hello","dear","coders","!")
# funargs(*har)

#OUTPUTt:
#hello
#dear
#coders

#3. Passing normal argument then *arg argument.'
# def funargs(normal,*args):
#     print(normal)
#     for x in args:
#         print(x)
# normal="I am a normal argument and the students are:"
# har=("hello","dear","coders","!")
# funargs(normal, *har)

#-but if we pass a normal argument after *args : will show an error
 
# def funargs(*args, normal):
#     print(normal)
#     for x in args:
#         print(x)
# normal="I am a normal argument and the students are:"
# har=("hello","dear","coders","!")
# funargs( *har,normal)  #error

#3. **kwargs:
# def kfunc(**kwargs):
#     for x, y in kwargs.items():
#         print("%s==%s"%(x,y))

# kfunc(Mum='Bells',Dad="John",Sis="Cassie")
#Output:
# Mum==Bells
# Dad==John
# Sis==Cassie

#4. **kwargs with other normal argument:
# def kfunc(**isa):
#     for x, y in isa.items():
#         print("%s==%s"(x,y))

# kfunc("Hi",Mum='Bells',Dad="John",Sis="Cassie")


#5. Using all these in combination:
# def funargs(normal,*args,**kwargs):
#     print(normal)
#     for x in args:
#         print(x)
#     print("My family:")
#     for y,z in kwargs.items():
#         print(f"{y} is a {z}")
# normal="I am a normal argument and the students are:"
# har=("hello","dear","coders","!")
# kar={"Dad":"John","Mom":"Bell","Sis":"Gig"}
# funargs(normal, *har,**kar)

#Ex 2:

# def myfunc(arg1,arg2,arg3):
#     print("arg1:",arg1)
#     print("arg2:",arg2)
#     print("arg3:",arg3)


# args=("Hello","Dear","Coders")
# myfunc(*args)

# kwargs={"arg1":"John","arg2":"Bell","arg3":"Gig"}
# myfunc(**kwargs)
#OUTPUT: 
# arg1: Hello
# arg2: Dear
# arg3: Coders
# arg1: John
# arg2: Bell
# arg3: Gig

#EX3: 
def myfunc(*args,**kwargs):
    print("Args:",args)   #Args: ('Hey', 'coders!')
    print("Kwargs:",kwargs)  #Kwargs: {'mom': 'bells', 'dad': 'John', 'sis': 'Catherine'}

myfunc('Hey','coders!',mom='bells',dad='John',sis='Catherine')
