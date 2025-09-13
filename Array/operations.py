# Counting elements
import array
a = array.array('i', [1, 2, 3, 4, 2, 5, 2])

count = a.count(2)
print(count)

# Reversing elements
import array
a = array.array('i', [1, 2, 3, 4, 5])

a.reverse()
print(*a)

# Extending elements
import array as arr 
a = arr.array('i', [1, 2, 3,4,5])

a.extend([6,7,8,9,10])
print(a)