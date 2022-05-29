from classes.car import Car
from classes.person import Person
import json
import os.path


class Employee(Person):

    def __init__(
            self,
            name=None,
            money=None,
            mood=None,
            healthRate=None,
            car=None,
            Id=None,
            email=None,
            salary=None,
            distanceToWork=None
    ):
        self._id = Id
        self._email = email
        self._salary = salary
        self._distanceToWork = distanceToWork
        self._car = car
        super(Employee, self).__init__(name, money, mood, healthRate)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, Id):
        self._id = Id

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    @property
    def distanceToWork(self):
        return self._distanceToWork

    @distanceToWork.setter
    def distanceToWork(self, distanceToWork):
        self._distanceToWork = distanceToWork

    @property
    def car(self):
        return self._car

    @car.setter
    def car(self, car):
        self._car = car

    def work(self, hours):
        if hours == 8:
            self.mood = 'happy'
        if hours < 8:
            self.mood = 'tired'
        if hours > 8:
            self.mood = 'lazy'

    def drive(self, distance=distanceToWork):
        self.distanceToWork = self.car.run(self.car.velocity, distance)
        if self.distanceToWork != 0:
            while True:
                choice = input("Fuel ? (y or n)")
                if choice == 'y':
                    self.refuel()
                    self.buy(10)
                    break
                else:
                    print("oh, you should click y quickly !!")

    def refuel(self, gasAmount=100):
        self.car.fuelRate = gasAmount

    def send_mail(self, to, subject, msg, receiver_name):
        if not os.path.isdir("emails"):
            os.mkdir("emails")

        email = {
            self.name: [
                {
                    "to": to,
                    "from": self.email,
                    "receiver name": receiver_name,
                    "subject": subject,
                    "message": msg,
                },
            ],
        }

        if not os.path.isfile(f"emails/{self.name}.json"):
            jsonData = json.dumps(email, indent=4)
            file = open(f"emails/{self.name}.json", "w")
            file.write(jsonData)
            file.close()
        else:
            with open(f"emails/{self.name}.json", "r+") as innerData:
                data = json.load(innerData)
                data[self.name].append(email[self.name][0])
                # print(type(data[self.name]))
                with open(f"emails/{self.name}.json", "w") as update:
                    update.seek(0)
                    json.dump(data, update, indent=4)

# test Employee class
# if __name__ == '__main__':
#     car = Car("fiat", 100, 0)
#     emp = Employee(
#         car=car,
#         name="Mohamed",
#         money=5000,
#         mood="happy",
#         healthRate=100,
#         Id=1,
#         distanceToWork=20,
#         salary=5000,
#         email="m@gmail.com"
#     )
#
#     print(emp.mood)
#     print(emp.name)
#     emp.sleep(2)
#     print(emp.mood)
#     emp.drive(20)
#     print(emp.car.carName)
#     print(emp.car.fuelRate)
#     emp.refuel()
#     print(emp.car.fuelRate)
#     emp.send_mail("x@gmail.com", "New Email", "Hello from email body", "Ahmed")
# emp.send_mail("y@gmail.com", "other Email", "Hello from thr other email body", "Munir")
# jsonFile = open(f"{emp.name}.json")
# jsonObject = json.load(jsonFile)
# print(jsonObject)
# print("json object type: " + str(type(jsonObject)))
# print("email subject: " + jsonObject[emp.email]["subject"])
