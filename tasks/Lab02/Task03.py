def myString(text):
    myList = []
    for i in text:
        myList.append(i)
    myList.reverse()
    print("".join(myList))


myString("Hello World")
