
print('Anushka Porwal')
print('Roll No.:0863CS241039')
print('text',6+3,4>5,type(3.14))
print('vote' if 19>18 else 'no vote')
print([i for i in range(0,5)])

name='Anushka'
age= 19
salary = 45000
print('my name is',name,'and my age is',age,'with the','salary',salary)
print(f'my name is {name} and my age is {age} with the salary {salary}')


print('''
------------------------------------------
PNB Bank
-----------------------------------------
1 ---> Account Details
2 ---> Account Balance
3 ---> Last 5 Transactions
4 ---> Cheque Book Request
5 ---> Feedback
------------------------------------------
''' )

a=6
pi=3.14
c=3+4j
print(a,pi,c)

what_inside_me=None

what_i_am=True

name='Anushka Porwal'

arr=[1,2,3,4,5,'hello',[11,22,33]]

print(arr[3])
print(arr[6][2])

tuple=(1,2,3,4,5)
print(tuple)

set={1,1,2,2,3,4,4,5}
print(set)

dict={
    'Fruit':['Apple','Mango'],
    'Climate':['cold','hot'],
    'Price':[120,80]
}

print(dict)
print(dict['Fruit'])
print(dict['Price'][1])

name=input('Enter your name: ')
print(name)
roll_no=int(input('Enter your roll number: '))
marks=float(input('Enter your marks: '))
sub=eval(input('Enter your subject: ')) # tuple or list 
print(type(name))


# 4 spaces after condition 
'''
 
if condition:                         
    statement
    statement
elseif condition 
    statement
    statement
else:
    statement
    statement
'''

if 5>3:
    print('It will be executed')
if 5>4:
    print('this is true')

elif 5<3:
    print('this will be executed')
else:
    print('bye')

age= int(input('Enter your age: '))
if age>=18:
    print('You are eligible for voting')
    if age>55:
        print('You are senior citizen')

    else:
        print('Youth Citizen')
elif age<=18 and age>0:
    print('You are not eligible for voting')

else:
    print('Invalid age')

    print('''
------------------------------------------  
    LETS PLAY ROCK PAPER SCISSOR
------------------------------------------
                Rules
              r--->p=p
              p--->s=s
              s--->r=r
------------------------------------------
''')    

u1=input('Player 1 enter your name: ')
u2=input('Player 2 enter your name: ')

c1=input(f'{u1} choice r/p/s: ')
c2=input(f'{u2} choice r/p/s: ')

if c1==c2:
    print('Match Draw')

elif((c2=='p' and c1=='r') or (c2=='s' and c1=='p') or (c2=='r' and c1=='s')):
    print(f'{u2} wins')

elif((c1=='p' and c2=='r') or (c1=='s' and c2=='p') or (c1=='r' and c2=='s')):
    print(f'{u1} wins')

else:
    print('Invalid Input')




