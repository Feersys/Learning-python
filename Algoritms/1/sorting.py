import random

# cum = []
# n = 40
# for i in range(n):
#    cum.append(random.randint(0, 500))
# print(cum)
# for i in range(n - 1):
#        if cum[j] > cum[j + 1]:
#            cum[j + 1], cum[j] = cum[j], cum[j + 1]
# print(cum)


# for i in range(1, n):
#    temp = cum[i]
#    j = i - 1
#    while (j >= 0 and temp < cum[j]):
#        cum[j + 1] = cum[j]
#        j -= 1
#    cum[j + 1] = temp
# print(cum)
cum = []
n = 40
for i in range(n):
    cum.append(random.randint(0, 500))
print(cum)


def quicksort(cum):

    print(cum)
    if len(cum) <= 1:
        return cum
    elem = cum[0]
    left = list(filter(lambda x: x < elem, cum))
    center = [i for i in cum if i == elem]
    right = list(filter(lambda x: x > elem, cum))
    return quicksort(left) + center + quicksort(right)

print(quicksort(cum))

def merge_sort(cum):
    if len(cum) > 1:
        mid = len(cum) // 2
        left = cum[:mid]
        right = cum[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                cum[k] = left[i]
                i += 1
            else:
                cum[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            cum[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            cum[k] = right[j]
            j += 1
            k += 1
    return cum

print(merge_sort(cum))
