import Auth.Login as log
import projects.MainScreen as main

file = open("projects/projects.txt", "r")
proData = file.readlines()
myList = []
for i in proData:
    myList.append(i.split(','))
file.close()


def myTracking():
    while True:
        selected = input("Press 1 to go back or 2 to exit: ")
        if selected == '1':
            main.mainScreen()
            break
        elif selected == '2':
            print("Thank You")
            break
        else:
            print("wrong answer .. try again")


def createNewProject():
    proTitle = input("Project Title: ")
    proDetails = input("Project Details: ")
    totalTarget = input("Project Total Target: ")
    startDate = input("Start Date: ")
    endDate = input("End Date: ")
    proData = {
        'user': log.userData[0][2],
        'title': proTitle,
        'details': proDetails,
        'target': totalTarget,
        'start': startDate,
        'end': endDate
    }
    proFile = open("projects/projects.txt", "a")

    proFile.writelines(
        f"{proData['user']},{proData['title']},{proData['details']},{proData['target']},{proData['start']},{proData['end']}\n")
    proFile.close()
    myTracking()


def viewAllProjects(currentUser):
    for j in range(0, len(myList)):
        if myList[j][0] == currentUser[0][2]:
            print(
                f"title : {myList[j][1]}, details: {myList[j][2]}, target: {myList[j][3]}, start Date: {myList[j][4]}, end Date: {myList[j][5]}")
            print("----------------------------------")
    myTracking()


def deleteProject(currentUser):
    projectName = input("Enter Project Name: ")
    flag = 0
    for i in range(0, len(myList)):
        if myList[i][0] == currentUser[0][2] and myList[i][1] == projectName:
            myList[i].clear()
            flag = 1
    if flag == 0:
        print("Project Not Found .. Make Sure From Name or It's Not exists")
    else:
        print(f"{projectName} deleted successfully >>")
    newFile = open("projects/projects.txt", "w")
    for j in range(0, len(myList)):
        newFile.writelines(','.join(myList[j]))
    myTracking()


def editProjectData(currentUser):
    print("Your Current Projects >>")
    viewAllProjects(log.userData)
    projectName = input("Enter Project Name to edit: ")
    flag = 0
    for i in range(0, len(myList)):
        if myList[i][0] == currentUser[0][2] and myList[i][1] == projectName:
            myList[i][1] = input("Title: ")
            myList[i][2] = input("Details: ")
            myList[i][3] = input("Target: ")
            myList[i][4] = input("Start Date: ")
            myList[i][5] = input("End Date: ")
            flag = 1
    if flag == 0:
        print("Project Not Found .. Make Sure From Name or It's Not exists")
    else:
        print(f"{projectName} updated successfully >>")
    newFile = open("projects/projects.txt", "w")
    for j in range(0, len(myList)):
        newFile.writelines(','.join(myList[j]))
    myTracking()
