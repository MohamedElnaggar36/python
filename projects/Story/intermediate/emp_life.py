from classes.car import Car
from classes.employee import Employee
import re


def mainScreen():
    emp = employeeData()

    print(f"    --    good morning {emp.name}, hope to be good today :)")
    while True:

        print("-------------------------------------------------------------")
        print("1. Edit your name")
        print("2. Change your balance amount")
        print("3. Sleep")
        print("4. Eat")
        print("5. Buy something")
        print("6. Change your car")
        print("7. View your profile")
        print("8. go to work")
        print("9. refuel your car")
        print("10. send email")
        print("11. Close")

        select = input("    -> enter your choice: ")
        if select.isdigit():
            select = int(select)
            if select == 1:
                emp.name = validateName()
                print(f"nice! welcome {emp.name},")
            elif select == 2:
                emp.money = validateBalance()
                print(f"your current balance: {emp.money}")
            elif select == 3:
                hours = validateSleep()
                emp.sleep(hours)
                print(f"your mood is: {emp.mood}")
            elif select == 4:
                meals = validateMeals()
                emp.eat(meals)
                print(f"your health rate is: {emp.healthRate}")
            elif select == 5:
                items = validateItems()
                emp.buy(items)
                print(f"your current balance: {emp.money}")
            elif select == 6:
                emp.car = validateCar()
                print(f"{emp.car.carName} ! wow that's a good choice")
            elif select == 7:
                viewProfile(emp)
            elif select == 8:
                gotoWork(emp)
                print(f"your current fuel: {emp.car.fuelRate}")
            elif select == 9:
                refuelCar(emp)
                print(f"your current fuel: {emp.car.fuelRate}")
            elif select == 10:
                sendEmail(emp)
            elif select == 11:
                print(f"thanks, {emp.name} see you soon :)")
                break
            else:
                print("     ! please select only from this order")
        else:
            print("     ! please enter a number of choice")


def employeeData():
    print("------- welcome, let's start your life story --------")
    name = validateName()
    email = validateEmail()
    mood = validateMood()
    healthRate = validateHealthRate()
    money = validateBalance()
    car = validateCar()

    return Employee(name=name, email=email, mood=mood, healthRate=healthRate, money=money, car=car, distanceToWork=20)


def validateName():
    while True:
        name = input("Name: ")
        if name.isdigit():
            print("     ! please enter a name not a number")
        elif len(name.strip()) <= 5:
            print("     ! name is too short !!")
        else:
            return name


def validateEmail():
    while True:
        email = input("Email: ")
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, email):
            return email
        else:
            print("Invalid Email, please check email format")


def validateMood():
    while True:
        select = input("select your mood (1.happy 2.tired 3.lazy): ")
        if not select.isdigit():
            print("     ! please enter number of choice only ..")
        elif int(select) == 1:
            return "happy"
        elif int(select) == 2:
            return "tired"
        elif int(select) == 3:
            return "lazy"
        else:
            print("     ! please enter a correct choice ..")


def validateHealthRate():
    while True:
        select = input("enter health rate (1- 100 2- 75 3- 50): ")
        if not select.isdigit():
            print("     ! please enter number of choice only ..")
        elif int(select) == 1:
            return 100
        elif int(select) == 2:
            return 75
        elif int(select) == 3:
            return 50
        else:
            print("     ! please enter a correct choice ..")


def validateBalance():
    while True:
        money = input("enter your money balance: ")
        if not money.isdigit():
            print("     ! please enter a number of balance only")
        else:
            return int(money)


def validateCar():
    while True:
        carName = input("enter your car name: ")
        if not carName.isdigit():
            fuelRate = input("enter current fuel rate: ")
            if fuelRate.isdigit():
                if int(fuelRate) in range(0, 101):
                    velocity = input("range of velocity you drive on: ")
                    if velocity.isdigit():
                        if int(velocity) in range(0, 201):
                            return Car(carName=carName, fuelRate=int(fuelRate), velocity=int(velocity))
                        else:
                            print("     ! velocity must be in range 0 to 200 only")
                    else:
                        print("     ! please enter number of velocity rate only")
                else:
                    print("     ! please enter fuel rate in range 0 to 100")
            else:
                print("     ! please enter number of fuel rate only")
        else:
            print("     ! please enter a valid name for the car")


def validateSleep():
    while True:
        sleepHours = input("how much will you sleep: ")
        if not sleepHours.isdigit():
            print("     ! please enter hours as number only")
        else:
            return int(sleepHours)


def validateMeals():
    while True:
        meals = input("select meals (1 - 2 - 3) meals: ")
        if not meals.isdigit():
            print("     ! please enter number of choice only")
        elif int(meals) == 1:
            return 1
        elif int(meals) == 2:
            return 2
        elif int(meals) == 3:
            return 3
        else:
            print("     ! please enter a correct choice of selection")


def validateItems():
    while True:
        items = input("enter amount of items you will buy: ")
        if items.isdigit():
            return int(items)
        else:
            print("     ! please enter number of bought items only")


def viewProfile(emp):
    print(
        f"----> Name: {emp.name} \n"
        f"----> Mood: {emp.mood} \n"
        f"----> Health rate: {emp.healthRate} \n"
        f"----> money: {emp.money} \n"
    )


def gotoWork(emp):
    while True:
        chDistance = input(
            f"distance to work is {emp.distanceToWork}  and velocity is {emp.car.velocity} change ? enter y or n: ")
        if chDistance == 'y':
            newDistance = input("new distance: ")
            if newDistance.isdigit():
                emp.distanceToWork = int(newDistance)
                chVelocity = input(f"velocity range is {emp.car.velocity} ? enter y or n: ")
                if chVelocity == 'y':
                    newVelocity = input("new velocity: ")
                    if newVelocity.isdigit():
                        emp.car.velocity = int(newVelocity)
                        emp.drive(emp.distanceToWork)
                        break
                    else:
                        print("     ! please enter velocity as number")
                elif chVelocity == 'n':
                    emp.drive(emp.distanceToWork)
                    break
                else:
                    print("     ! enter only y or n")
            else:
                print("     ! please enter distance in numbers only")
        elif chDistance == 'n':
            emp.drive(emp.distanceToWork)
            break
        else:
            print("     ! enter only y or n")


def refuelCar(emp):
    emp.refuel()
    emp.buy(10)


def sendEmail(emp):
    while True:
        print("please fill receiver info ->")
        receiverEmail = validateEmail()
        receiverName = validateName()
        subject = input("Subject: ")
        msg = input("Message: ")
        emp.send_mail(to=receiverEmail, receiver_name=receiverName, subject=subject, msg=msg)
        break


if __name__ == '__main__':
    mainScreen()
