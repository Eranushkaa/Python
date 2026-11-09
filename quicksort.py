#Quicksort


def quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = arr[(start + end) // 2]
    i = start
    j = end

    while i <= j:
        while arr[i] < pivot:
            i = i + 1

        while arr[j] > pivot:
            j = j - 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
            j = j - 1

    if start < j:
        quick_sort(arr, start, j)

    if i < end:
        quick_sort(arr, i, end)


arr = eval(input('Enter your elements: '))
print(f'Unsorted array: {arr}')

quick_sort(arr, 0, len(arr) - 1)

print(f'Sorted array: {arr}')


#///////////////////////////////////////////////////
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    else:
        pivot = arr[0]

        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)          

    arr = eval(input('Enter your elements: '))
print(f'Unsorted array: {arr}')

quick_sort(arr, 0, len(arr) - 1)

print(f'Sorted array: {arr}')

    arr = eval(input('Enter your elements: '))
print(f'Unsorted array: {arr}')

quick_sort(arr, 0, len(arr) - 1)

print(f'Sorted array: {arr}')

