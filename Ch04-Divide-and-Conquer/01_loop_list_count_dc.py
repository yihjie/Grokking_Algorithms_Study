def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

print([2, 3, 4, 5])
print(count([2, 3, 4, 5]))