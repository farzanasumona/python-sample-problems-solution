lst = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
    element = int(input())
    lst.append(element)

print(lst)

for x in lst:
    if x % 2 == 0:
        print(x, end=" ")

