from classes.car import Car
from classes.employee import Employee
from classes.office import Office
import intermediate.emp_life as valid


def mainScreen():
    office = officeData()
    print(f"------- welcome, in {office.name} office -------")

    while True:
        print("------------------------------------------------")
        print("1. Display all employees")
        print("2. Display an employee")
        print("3. Get employees count")
        print("4. Hire")
        print("5. Fire")
        print("6. Reward")
        print("7. Deduct")
        print("8. Check Lateness")
        print("9. Close")

        select = input("    -> enter your choice: ")
        if select.isdigit():
            select = int(select)
            if select == 1:
                office.get_all_employees()
            elif select == 2:
                Id = input("employee id to find: ")
                if not validNum(Id):
                    print("     ! please enter id as number only")
                else:
                    office.get_employee(int(Id))
            elif select == 3:
                print(office.getEmployeesNum())
            elif select == 4:
                emp = hireEmp()
                office.hire(emp)
            elif select == 5:
                empId = input("enter employee id to fire: ")
                if not validNum(empId):
                    print("     ! please enter id as number only")
                else:
                    office.fire(int(empId))
            elif select == 6:
                rewardEmp(office)
            elif select == 7:
                deductEmp(office)
            elif select == 8:
                applyLateness(office)
            elif select == 9:
                print(f"time to close {office.name}, :) see you next")
                break
            else:
                print("     ! please select only from this order")
        else:
            print("     ! please enter a number of choice")


def officeData():
    print("first we need a name for this office :)")
    officeName = input("Office Name: ")
    return Office(officeName)


def hireEmp():
    print("please fill employee data >>")
    while True:
        empName = valid.validateName()
        Id = input("id: ")
        if validNum(Id):
            email = valid.validateEmail()
            salary = input("salary: ")
            if validNum(salary):
                return Employee(name=empName, Id=int(Id), email=email, salary=int(salary))
            else:
                print("     ! salary must be a number only")
        else:
            print("     ! id must be a number only")


def validNum(num):
    return num.isdigit()


def rewardEmp(office):
    while True:
        empId = input("enter employee id to reward: ")
        reward = input("enter amount to reward: ")
        if validNum(empId) and validNum(reward):
            office.reward(empId=int(empId), reward=int(reward))
            break
        else:
            print("Make sure that to enter numbers only not strings")


def deductEmp(office):
    while True:
        empId = input("enter employee id to deduct: ")
        deduct = input("enter amount to deduct: ")
        if validNum(empId) and validNum(deduct):
            office.deduct(empId=int(empId), deduct=int(deduct))
            break
        else:
            print("Make sure that to enter numbers only not strings")


def loadEmployees(office):
    return office.get_all_employees()


def getEmployeeData(office, empId):
    data = loadEmployees(office)
    user = None
    flag = 0
    for i in range(0, len(data[office.name])):
        if data[office.name][i]["id"] == empId:
            user = data[office.name][i]
            flag = 1
    if flag == 1:
        return user
    else:
        return 0


def applyLateness(office):
    while True:
        empId = input("enter employee id: ")
        if not validNum(empId):
            print("     ! please enter a number for id")
        else:
            user = getEmployeeData(office, int(empId))
            if user != 0:
                moveHour = input("enter move hour: ")
                if not validNum(moveHour):
                    print("     ! please enter move hour as numbers only ")
                else:
                    velocity = input("enter car velocity: ")
                    if not validNum(velocity):
                        print("     ! car velocity must be numbers only")
                    else:
                        fuelRate = input("enter fuel rate: ")
                        if not validNum(fuelRate):
                            print("     ! fuel rate must be numbers only")
                        else:
                            distance = input("enter distance to work: ")
                            if not validNum(fuelRate):
                                print("     ! distance to wor must be numbers only")
                            else:
                                office.check_lateness(
                                    empId=int(empId),
                                    moveHour=int(moveHour),
                                    employee=Employee(
                                        name=user['employee name'],
                                        Id=user['id'],
                                        email=user['email'],
                                        salary=user['salary'],
                                        car=Car(
                                            carName="fiat",
                                            velocity=int(velocity),
                                            fuelRate=int(fuelRate)
                                        ),
                                        distanceToWork=int(distance))
                                )
                                break
            else:
                print("     ! employee not found with this id")


if __name__ == '__main__':
    mainScreen()
