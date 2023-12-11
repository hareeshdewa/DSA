# Linear Search:

def linear_search(nums : list[int],target):
    for num in range(len(nums)):
        if nums[num] == target:
            print("Linear Search: ",num)
    return -1
linear_search([9,1,8,3,2,4,5,7],4)
print()


# Binary Search:
def binary_search(nums: list[int],target):
    starting_index = 0
    ending_index = len(nums) - 1

    while starting_index <= ending_index:
        middle_index = (starting_index + ending_index) // 2
        value = nums[middle_index]
        print("middle: ", value)

        if value < target:
            starting_index = middle_index + 1
        elif value > target:
                ending_index = middle_index - 1
        else:
            return middle_index
    return -1
print("Binary Search:")
print(binary_search([9,4,32,12,54,330,980,122],330))
print(binary_search([34,54,21,67,88,98,212],54))
print(binary_search([121,1212,43,56,88,908,422],88))
print(binary_search([32,77,65,432,12,1000],65))
print()

# bubble sort:
def bubble_sort(nums: list[int]):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
        num = ''.join(map(str,nums))
    print("Bubble Sort: ",num)
bubble_sort([9,1,8,2,7,3,6,4,5])
print()

# Selection Sort:

def selection_sort(nums: list[int]):
    for i in range(len(nums)):
        # current minimum
        min = i
        for j in range(i+1,len(nums)):
            if nums[min] > nums[j]:
                min = j
        temp = nums[i]
        nums[i] = nums[min]
        nums[min] = temp
        num = ''.join(map(str,nums))
    print("selection sort: ",num)


selection_sort([8,7,9,2,3,1,5,4,6])
print()
# Insertion Sort:

def insertion_sort(nums: list[int]):
    for i in range(1,len(nums)):
        temp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > temp:
            nums[j+1] = nums[j]
            j = j - 1

        nums[j+1] = temp
    num = "".join(map(str,nums))

    print("insertion Sort : ",num)

insertion_sort([9,1,8,2,7,3,6,5,4])
print()

def mergeSort(nums):
    length = len(nums)
    if length <=1:
        return nums

    middle = length // 2
    left_array = nums[:middle]
    right_array = nums[middle:]

    mergeSort(left_array)
    mergeSort(right_array)
    merge(left_array,right_array,nums)

def merge(left_array,right_array,nums):
    leftsize = len(left_array)
    rightsize = len(right_array)
    i = 0
    l = 0
    r = 0
    # indices
    while l < leftsize and r < rightsize:
        if left_array[l] < right_array[r]:
            nums[i] = left_array[l]
            l +=1
        else:
            nums[i] = right_array[r]
            r+=1
        i+=1
    while l < leftsize:
        nums[i] = left_array[l]
        i+=1
        l+=1
    while r < rightsize:
        nums[i] = right_array[r]
        i+=1
        r+=1
nums = [9, 3, 2, 4, 5, 1, 6, 7, 8]
mergeSort(nums)
print("Merge Sort: ",''.join(map(str,nums)))
print()










