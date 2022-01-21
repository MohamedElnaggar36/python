# 6. Write a program that generate a multiplication table from 1 to the number passed
num = 3
newList = []
for row in range(num):
    innerList = []
    for col in range(row + 1):
        result = (col + 1) * (row + 1)
        innerList.append(result)
    newList.append(innerList)
print(newList)