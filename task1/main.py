import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

list_a = []
list_a.append(1)

for i in range(1000):
    num = list_a[i] + m - 1
    if num > n:
        num -= n
    if num != 1:
        list_a.append(num)
    if num == 1:
        break

print(list_a)
