import intermediate.emp_life as emp
import intermediate.office_life as office


def mainStory():
    print("Welcome Hero :) who are you now >>")
    while True:
        print("1. Employee Story")
        print("2. Office Story")
        select = input("enter your choice: ")
        if select == '1':
            emp.mainScreen()
            break
        elif select == '2':
            office.mainScreen()
            break
        else:
            print("oops :) try again and enter only 1 or 2")


if __name__ == '__main__':
    mainStory()
