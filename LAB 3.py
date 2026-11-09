for i in range(1, 10, 2):
    print(i)


name = 'Anushka Porwal'
for i in name:
    print(i)


arr = [10, 20, 30, 40, 50, 60]
for a in arr:
    print(a)


num = int(input('Enter a number: '))
digit = str(num)
count = 1 
largest = 1

for a in range(1, len(digit)):
    if int(digit[a]) == int(digit[a-1])+1:
        count += 1

    else:
        count = 1

    if count > largest:
        largest = count      

print(count)


hr = int(input("Enter hour: "))
min = int(input("Enter minute: "))

if hr >= 24 or min >= 60:
    print("Invalid time")

elif hr >= 12:
    if hr == 12:
        print(f"{hr}:{min} PM")
    else:
        print(f"{hr-12}:{min} PM")

else:
    print(f"{hr}:{min} AM")


for i in range(1, 5):
    for j in range(1, 5):
        if i==j or i<j:
            print('*',end=' ')

    print()
for i in range(0, 4):
    for j in range(0, 4):
        if i==j or i>j:
            print('*',end=' ')

    print() 


size=(int(input('Enter the size of the square: ')))
for i in range(size):
    for j in range(size):
        if i == 0 or i == size-1 or j == 0 or j == size-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()


size = int(input("Enter the size: "))

for i in range(size):
    for j in range(size):
        if (i == 0 or i == size//2 or i == size-1 or
            j == 0 or j == size-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


    size = int(input("Enter the size: "))

for i in range(size):
    for j in range(size):
        if i == 0 or i == size-1 or j == 0 or j == size-1 or i == size//2 or j == size//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


    size = int(input("Enter the size: "))

for i in range(size):
    for j in range(size):
        if i == j or i + j == size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

    size = int(input("Enter the size: "))

for i in range(size):
    for j in range(2 * size - 1):
        if j >= size - 1 - i and j <= size - 1 + i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


sum=0
while True:
    num=int(input("Enter a number: "))
    sum=sum+num

    if num==0:
        break
    print("Sum of numbers is:",sum)



num = int(input("Enter number: "))

while num >= 10:
    sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum = sum + digit
        rem = rem // 10

    print(num, "->", sum)
    num = sum

print("Single digit =", num)