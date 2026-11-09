print("Roll No.: 0863CS241039")
print("Name: Anushka Porwal")
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        l = r = k = 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                arr[k] = left[l]
                l += 1
            else:
                arr[k] = right[r]
                r += 1
            k += 1

        while l < len(left):
            arr[k] = left[l]
            l += 1
            k += 1

        while r < len(right):
            arr[k] = right[r]
            r += 1
            k += 1

arr = eval(input("Enter the list of numbers: "))
print("Unsorted array:", arr)

merge_sort(arr)

print("Sorted array:", arr)


