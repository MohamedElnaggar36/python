from projects.MainScreen import mainScreen

content_List = []
userData = []
flag = 0


def readAllData():
    global content_List
    file = open("Auth/users.txt", "r")
    content = file.read()
    content_List = content.splitlines()
    file.close()


def checkData(email, password):
    global flag
    readAllData()
    for i in range(0, len(content_List)):
        data = content_List[i].split(':')
        if data[2] == email and data[3] == password:
            userData.append(data)
            print("Successfully Login >>")
            flag = 1
            mainScreen()
    if flag == 0:
        print("email not found or password not correct ..!")


def mainLogin():
    while True:
        userEmail = input("Email: ")
        userPass = input("Password: ")
        checkData(userEmail, userPass)
        if flag == 1:
            break
