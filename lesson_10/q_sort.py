from random import randint


def quick_sort(nums, first_idx_el, last_idx_el):
    if first_idx_el >= last_idx_el:
        return

    i, j = first_idx_el, last_idx_el
    middle_value = nums[(first_idx_el + last_idx_el) // 2]

    while i <= j:
        while nums[i] < middle_value:
            i += 1
        while nums[j] > middle_value:
            j -= 1

        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1

    quick_sort(nums, first_idx_el, j)
    quick_sort(nums, i, last_idx_el)


lst = [randint(0, 100) for _ in range(35)]
print(lst)
quick_sort(lst, 0, len(lst)-1)
print(lst)
