import random


def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        ii = j = k = 0
        while ii < len(left_half) and j < len(right_half):
            if left_half[ii] < right_half[j]:
                lst[k] = left_half[ii]
                ii += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1
        while ii < len(left_half):
            lst[k] = left_half[ii]
            ii += 1
            k += 1
        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1
    return lst


my_list = []
for i in range(10):
    my_list.append(random.randint(0, 999))
print("ARRAY BEFORE SORTING")
print(my_list)
'''print(len(my_list)//2)
print(my_list[:len(my_list)//2])'''
print("ARRAY AFTER SORTING")
print(merge_sort(my_list))
