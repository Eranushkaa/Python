print('Anushka Porwal')
print('Roll No.:0863CS241039')

l1=[] #empty list
l2=[1,2,3,4,5] 
print(l1,l2)

print(2 not in l2)


#iterate each element in the list
for a in l1:
    print(a)

for a in range(0,len(l2)):
    print(l2[a])

#operations in list 
#addition of list 

l1=[4,5,6,7,8]
l3=l1+l2
print(l3)
l4=l2+l1
print(l4)

#MULTIPLICATION OF LIST
l5=l2*3
print(l5)

l1.pop() #removes last element
print(l1)

l1.append(50) #adds element at the end
print(l1)

l1.remove(5) #removes the first occurrence of 5
print(l1)

l2=[1,2,3,4,4,4,5,6,]
print(l2.count(4)) #counts the number of occurrences of 4 in the list

print(max(l2)) #returns the maximum value in the list
print(min(l2)) #returns the minimum value in the list

print(l2.sort()) #sorts the list in ascending order
print(l2)

#list comprehension
#new_list=[expression for item in iterable if condition]
l1=[5,6,7,8,9]
l2=[]
for a in l1:
    l2.append(a*a)
print(l2)

my_list=[a*a for a in l1]
print(my_list)

#conditional list comprehension
my_list=[a*a for a in l1 if a%2==0]
print(my_list)

#Slicing of list -----> L[start:stop:step]
l1=[10,20,30,40,50,60]
print(l1[-3:]) #prints last 3 elements
print(l1[:5]) #prints elements from index 0 to 3
print(l1[1:4]) #prints elements from index 1 to 3
print(l1[3:]) #prints elements from index 3 to end
print(l1[1:5:2]) #prints elements from index 1 to 4 with step 2
print(l1[::-1]) #prints the list in reverse order

print(l1[-6:-2]) #prints elements from index -6 to -3
print(l1[-2:-6])
print(list)

