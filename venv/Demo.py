import os
import sys

print("hello")
print(os.path.dirname(sys.executable))

for a in range(1, 10, 2):
    print(a)
# pdb.setTrace()
data = [1, 3, 2, 4]
data.sort()
print(data)
data.insert(-1, 5)
print(data)
data.remove(3)
print(data)
