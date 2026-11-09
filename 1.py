def sum (a,b):
    sum=a+b
    print(sum)
    return sum

result=sum(b=10,a=200)
print(sum(10,20))

def result(a,b):
    sum=a+b
    multi=a*b
    return sum, multi


r1,r2=result(10,20)
print(r1)
print(r2)

#pass Employee ID and Employee Name as arguments to a function

def employee(id, e_name):
    print(f'ID: {id} / Employee Name: {e_name}')

employee(id=101, e_name='John Doe')

#.............................................................

def sum(*element):
    sum = 0

    for a in element:
        sum += a

    return sum

r1 = sum(10, 20, 30, 40, 50)

print(r1)

#..........................................................
def error_log(first,*all):
    print(f'[(first)]', *all)

error_log('2026-10-27 11:30', 'esp32 connection failed','time out')

#.........................................................

def sum(*all,sign=1):
    pass

sum(10,20,30,40,50,60,70,sign=-1)

#.........................................................
def sum(*all, sign=1):
    total = 0

    for a in all:
        total += a

    return sign * total

r = sum(10, 20, 30, 40, 50, 60, 70, sign=-1)

print(r)  
print(sum())

#..........................................................

def print_anything(**data):
    for key, value in data.items():
        print(f'{key} : {value}')


print_anything(name='Anushka Porwal')

print_anything(id=1001, e_name='Anushka', company='google', salary=1000000)

#.........................................................

#single expresion at a time using lambda function
sum=lambda a,b: a+b
print(sum(10,20))

root=lambda a: a*a
print(root(10))

greater=lambda a,b: a if a>b else b
print(greater(10,20))

greater=lambda a,b,c: a if a>b and a>c else (b if b>c else c)
print(greater(10,20,30))

#..........................................................

l1=[10,20,30,40,50]
l2=list(map(lambda a: a*a, l1))
print(l2) #pipelinning

l1=[1,2,3,4,5]
l2=list(filter(lambda a: a%2==0, l1))
print(l2) 


l1=[10,20,30,40,50,60,70,80,90,100]
l2=list(filter(lambda a: a>50, l1))
print(l2) 

#..........................................................












