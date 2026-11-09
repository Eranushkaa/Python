print("Roll No.: 0863CS241039")
print("Name: Anushka Porwal")
d1={}
d2={'name':['Anushka','Priya' ],   
    'dept':['CSE','AIDS'],
    'place':['Indore','Dewas'],
    'salary': [50000, 60000],
          

}
print(d2['name'][1])

for a in d2.keys():
    print(a)

for b in d2.values():
    print(b[0])
    print(b[1])

for a,b in d2.items():
     print(a)
     print(b)