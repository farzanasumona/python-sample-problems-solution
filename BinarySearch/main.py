x = [11, 22, 33, 44, 55]

n = int(input("Enter number to search: "))
lower = 0
upper = len(x)-1

while lower <= upper:
    mid = (lower+upper)//2
    if x[mid] == n:
        print("Number is in", mid+1, "location")
        break
    elif x[mid] > n:
        upper = mid-1

    else:
        lower = mid+1

if lower > upper:
    print("Number is not available.")
