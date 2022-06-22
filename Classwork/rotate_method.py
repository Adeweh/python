def rotate(list_to_rotate: list[int], rotate_by: int) -> list[int]:
    rotate_by = rotate_by % len(list_to_rotate)
    return list_to_rotate[rotate_by:] + list_to_rotate[:rotate_by]


# def rotate(lst, k):
#     k = k % len(lst)
#     return lst[k:] + lst[:k]


lst = [7, -3, 2, 4, 9]
print(rotate(lst, 8))
