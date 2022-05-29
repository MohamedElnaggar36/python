class Person:

    def __init__(self, name=None, money=None, mood=None, healthRate=None):
        self._name = name
        self._money = money
        self._mood = mood
        self._healthRate = healthRate

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, money):
        self._money = money

    @property
    def mood(self):
        return self._mood

    @mood.setter
    def mood(self, mood):
        self._mood = mood

    @property
    def healthRate(self):
        return self._healthRate

    @healthRate.setter
    def healthRate(self, healthRate):
        self._healthRate = healthRate

    def sleep(self, hours):
        if hours == 7:
            self.mood = 'happy'
        if hours < 7:
            self.mood = 'tired'
        if hours > 7:
            self.mood = 'lazy'

    def eat(self, meal):
        if meal == 1:
            self.healthRate = 50
        elif meal == 2:
            self.healthRate = 75
        else:
            self.healthRate = 100

    def buy(self, items):
        currentMoney = self.money
        totalCost = items * 10
        print(f"it costs {totalCost}")
        if self.money < totalCost:
            print("No more money ..")
        else:
            choice = input("press 1 to confirm payment, or 0 to cancel: ")
            if choice == '1':
                currentMoney -= totalCost
                self.money = currentMoney
            elif choice == '0':
                print("process canceled..")
            else:
                print("please enter a correct choice..")


# if __name__ == '__main__':
    # p1 = Person(name="Mohamed", money=5000, mood="happy", healthRate=100)
    #
    # print(f"name: {p1.name}, \nmoney: {p1.money}, \nmood: {p1.mood}, \nhealth-rate: {p1.healthRate}")
    #
    # p1.buy(5)
    # print(f"current money amount: {p1.money}")
