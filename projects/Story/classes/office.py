from classes.car import Car
from classes.employee import Employee

import json
import os.path


class Office:
    __employeesNum = 0  # class member

    @classmethod  # increase or decrease employees num
    def change_emps_num(cls, num):
        cls.__employeesNum += num

    def __init__(
            self,
            name,
            employees=None
    ):
        self._name = name
        self._employees = employees

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def employees(self):
        return self._employees

    @employees.setter
    def employees(self, employees):
        self._employees = employees

    def get_all_employees(self):
        if os.path.isfile(f"offices/{self.name}Data.json"):
            file = open(f"offices/{self.name}Data.json", "r+")
            fileData = json.load(file)
            for i in range(0, len(fileData[self.name])):
                print(
                    f"{i + 1} - "
                    f"Employee name: {fileData[self.name][i]['employee name']}, "
                    f"id: {fileData[self.name][i]['id']}, "
                    f"email: {fileData[self.name][i]['email']}, "
                    f"salary {fileData[self.name][i]['salary']}"
                )
            self.__employeesNum = len(fileData[self.name])
            return fileData
        else:
            print("no data found for this office..")

    def getEmployeesNum(self):
        if os.path.isfile(f"offices/{self.name}Data.json"):
            with open(f"offices/{self.name}Data.json", "r+") as file:
                fileData = json.load(file)
                self.__employeesNum = len(fileData[self.name])
                if self.__employeesNum == 0:
                    return f"no employees found in {self.name}"
                else:
                    return f"current employees number: {self.__employeesNum}"
        else:
            return "no data found for this office.."

    def get_employee(self, empId):
        if os.path.isfile(f"offices/{self.name}Data.json"):
            file = open(f"offices/{self.name}Data.json", "r+")
            fileData = json.load(file)
            flag = 0
            for i in range(0, len(fileData[self.name])):
                if fileData[self.name][i]['id'] == empId:
                    flag = 1
                    print(
                        f"{i + 1} - "
                        f"Employee name: {fileData[self.name][i]['employee name']}, "
                        f"id: {fileData[self.name][i]['id']}, "
                        f"email: {fileData[self.name][i]['email']}, "
                        f"salary {fileData[self.name][i]['salary']}"
                    )
            if flag == 0:
                print("employee not found..")
        else:
            print("no data found for this office..")

    def hire(self, employee):
        if not os.path.isdir("offices"):
            os.mkdir("offices")

        employeeData = {
            self.name: [
                {
                    "employee name": employee.name,
                    "id": employee.id,
                    "email": employee.email,
                    "salary": employee.salary
                }
            ]
        }
        if not os.path.isfile(f"offices/{self.name}Data.json"):
            jsonData = json.dumps(employeeData, indent=4)
            file = open(f"offices/{self.name}Data.json", "w")
            file.write(jsonData)
            file.close()
            Office.change_emps_num(1)
            print(f"{employeeData[self.name][0]['employee name']} is hired successfully")
        else:
            with open(f"offices/{self.name}Data.json", "r+") as innerData:
                data = json.load(innerData)
                data[self.name].append(employeeData[self.name][0])
                with open(f"offices/{self.name}Data.json", "w") as update:
                    update.seek(0)
                    json.dump(data, update, indent=4)
                    Office.change_emps_num(1)
                    print(f"{employeeData[self.name][0]['employee name']} is hired successfully")

    def fire(self, Id):
        if os.path.isfile(f"offices/{self.name}Data.json"):
            file = open(f"offices/{self.name}Data.json", "r+")
            fileData = json.load(file)
            flag = 0
            for i in range(0, len(fileData[self.name])):
                if fileData[self.name][i]['id'] == Id:
                    del fileData[self.name][i]
                    with open(f"offices/{self.name}Data.json", "w") as update:
                        json.dump(fileData, update, indent=4)
                    Office.change_emps_num(-1)
                    flag = 1
            if flag == 1:
                print("employee deleted..")
            else:
                print("employee not found..")
        else:
            print("no data found for this office..")

    def check_lateness(self, empId, moveHour, employee):
        if os.path.isfile(f"offices/{self.name}Data.json"):
            file = open(f"offices/{self.name}Data.json", "r+")
            fileData = json.load(file)
            flag = 0
            for i in range(0, len(fileData[self.name])):
                if fileData[self.name][i]['id'] == empId:
                    flag = 1
                    if Office.calculate_lateness(9, moveHour, employee.distanceToWork, employee.car.velocity):
                        self.reward(empId, 10)
                    else:
                        self.deduct(empId, 10)
            file.close()
            if flag == 0:
                print("employee not found")
        else:
            print("no data found for this office..")

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        if velocity == 0:
            return False
        else:
            timeTaken = distance / velocity
            arriveTime = timeTaken + moveHour
            return targetHour >= arriveTime

    def deduct(self, empId, deduct):
        if os.path.isfile(f"offices/{self.name}Data.json"):
            file = open(f"offices/{self.name}Data.json")
            fileData = json.load(file)
            user = None
            flag = 0
            for i in range(0, len(fileData[self.name])):
                if fileData[self.name][i]["id"] == empId:
                    fileData[self.name][i]["salary"] -= deduct
                    user = fileData[self.name][i]
                    with open(f"offices/{self.name}Data.json", "w") as update:
                        json.dump(fileData, update, indent=4)
                    flag = 1
            if flag == 1:
                print(f"{user['employee name']}, id = {user['id']} deducted successfully..")
            else:
                print("employee not found..")
        else:
            print("no data found for this office")

    def reward(self, empId, reward):
        if os.path.isfile(f"offices/{self.name}Data.json"):
            file = open(f"offices/{self.name}Data.json")
            fileData = json.load(file)
            user = None
            flag = 0
            for i in range(0, len(fileData[self.name])):
                if fileData[self.name][i]["id"] == empId:
                    fileData[self.name][i]["salary"] += reward
                    user = fileData[self.name][i]
                    with open(f"offices/{self.name}Data.json", "w") as update:
                        json.dump(fileData, update, indent=4)
                    flag = 1
            if flag == 1:
                print(f"{user['employee name']}, id = {user['id']} rewarded successfully..")
            else:
                print("employee not found..")
        else:
            print("no data found for this office")

# test Office class
# if __name__ == '__main__':
#     office1 = Office("iti")
#     office2 = Office("mti")
#     print(office1.getEmployeesNum())
# office1.hire(Employee("mohamed", 250000, "happy", 100, Car("fiat", 100, 0), 1, "emp@gmail.com", 2000, 20))
# office1.hire(Employee("ahmed", 250000, "happy", 100, Car("fiat", 100, 0), 2, "emp@gmail.com", 3000, 20))
# office2.hire(Employee("Ahmed", 250000, "happy", 100, Car("fiat", 100, 0), 2, "ahmed@gmail.com", 2000, 20))
# office1.reward(1, 1000)
# office1.deduct(1, 500)
# emp = Employee("ahmed", 250000, "happy", 100, Car("fiat", 100, 60), 2, "emp@gmail.com", 3000, 20)
#
# office1.check_lateness(2, 8, emp)
# office1.get_all_employees()
# office1.get_employee(1)
# office1.fire(2)
