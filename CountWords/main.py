words = 0

f = open("text.txt", "r")
data = f.read()
print(data)
lines = data.split()

words += len(lines)
print("Number of words:", words)