print('Anushka Porwal')
print('Roll No.:0863CS241039')


list1 = [10, 20, 30, 40, 50, 60]

result = list1[:3] + list1[3:][::-1]

print(result)


list1 = [10, 20, 30, 40, 50, 60]

k = int(input("Enter the value of k: "))
k=len(list1)%k
l2=list1[-k:] + list1[:-k]


print(l2)

list1 = [10, 20, 30, 40, 50, 60]

k = 3
k = k % len(list1)

result = list1[-k:] + list1[:-k] 
print(result)


list1 = [10, 20, 10, 30, 20, 40, 30]

result = []

for x in list1:
    if x not in result:
        result.append(x)

print(result)


a = [10, 20, 10, 30, 40, 20, 50]

for i in a:
    if a.count(i) == 1:
        print(i)          #30,40,50 
        


