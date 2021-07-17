def find_small_num(li, kth):
    li = sorted(li)
    return li[kth - 1]


def partition(li, l, r):
    x = li[r]
    i = l
    for j in range(l, r):
        if li[j] <= x:
            li[i], li[j] = li[j], li[i]
            i += 1

    li[i], li[r] = li[r], li[i]
    return i


def kth_smallest(li, l, r, k):

    if k > 0 and k <= r - l + 1:
        index = partition(li, l, r)
        if index - l == k - 1:  # The index of the 1st smallest is 0.
            return li[index]
        if index - l > k - 1:
            return kth_smallest(li, l, index - 1, k)
        return kth_smallest(li, index + 1, r, (k - 1) - (index - l))


li = [3, 5, 7, 56, 2, 6, 8]
print(kth_smallest(li, 0, len(li) - 1, 7))
