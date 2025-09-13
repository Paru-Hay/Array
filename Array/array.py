a = ([1, 2, 3, 4])
print([x * 2 for x in a])

res = [[1, 2], [3, 4]]
result = [[x * 2 for x in row] for row in res]
print(result)