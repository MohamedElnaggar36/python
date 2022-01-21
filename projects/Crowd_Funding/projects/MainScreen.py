from projects.projects_control import viewAllProjects, deleteProject, createNewProject, editProjectData
import Auth.Login as log


def mainScreen():
    print("<---- Crud Funding ---->")
    print("1. Create New Project")
    print("2. View All Projects")
    print("3. Edit Your Project")
    print("4. Delete A Project")
    print("5. Close")
    while True:
        select = input("Select What You Want >> ")
        if select == '1':
            createNewProject()
            break
        elif select == '2':
            viewAllProjects(log.userData)
            break
        elif select == '3':
            editProjectData(log.userData)
            break
        elif select == '4':
            deleteProject(log.userData)
            break
        elif select == '5':
            print("Thank You")
            break
        else:
            print("Invalid Choice.. try again")
