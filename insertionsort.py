print('Anushka Porwal')
print('Roll No.:0863CS241039')

#Insertion sort 

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j=i-1
        temp=arr[i]
        while temp < arr[j] and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp 

arr = eval(input('Enter your elements: '))
print(f'Unsorted array: {arr}')

insertion_sort(arr)

print(f'Sorted array: {arr}')