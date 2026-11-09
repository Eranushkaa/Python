print('Anushka Porwal')
print('Roll No.:0863CS241039')


#bubble sort algorithm
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

arr = eval(input('Enter your elements: '))
print(f'Unsorted array: {arr}')

bubble_sort(arr)

print(f'Sorted array: {arr}')
