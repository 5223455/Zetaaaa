list=[22,24,31,44]
res = [i for i in list if i<4]
print(res)
res = [i for i  in list if i%2 == 0]
print(res)
#upper case
words = ["hello","world","this","is","python"]
uppercase=[i.upper() for i in words]
print(uppercase)
#lower case
words = ['HELLO', 'WORLD', 'THIS', 'IS', 'PYTHON']
lowercase=[i.lower() for i in words]
print(lowercase)
#creating dictionary comphrehension from two lists
keys =['name', 'age', 'city']
values = ['Saketh', '19', 'hyd']
dictonary ={k:v for k,v in zip(keys,values)}
print(dictonary)

