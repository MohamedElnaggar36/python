def myFunction(length, start):
    myList = []
    for i in range(0, length):
        num = i + start
        myList.append(num)
    print(myList)


myFunction(5, 1)
