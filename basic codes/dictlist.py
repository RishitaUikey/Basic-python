'''1. how to add list in the dictionary 
2. how to print perticular variable in the dictionary
3.how to add another variable in the dictionary without 
adding in the dictonary and print key values  
4. print variable value of dictionary
5.use of x.items
6. How to delete varaible from the dictionary '''


'''x={'a':[1,2,3,4,5,6,7,8],
   'b':9,
   'c':15}
print(x)'''

'''x={'a':[1,2,3,4,5,6,7,8],
   'b':9,
   'c':15}
print(x['a'])'''

'''x={'a':[1,2,3,4,5,6,7,8],
   'b':9,
   }
x['c']=15
print(x.keys())
for i in x.keys():
    print(x[i])'''
    
'''x={'a':[1,2,3,4,5,6,7,8],
   'b':9,
   }
x['c']=15

for i in x.keys():
    print(x[i])'''
    
'''x={'a':[1,2,3,4,5,6,7,8],
   'b':9,
   }
x['c']=15
for i in x.items():
    print(i)'''
    
x={'a':[1,2,3,4,5,6,7,8],
   'b':9,
   }
x['c']=15
del(x['a'])
print(x)
    

    
