def divisableNum(num):
    byThree = "Fizz"
    byFive = "Buzz"
    if num % 3 == 0 and num % 5 != 0:
        return byThree
    elif num % 5 == 0 and num % 3 != 0:
        return byFive
    elif num % 3 == 0 and num % 5 == 0:
        return byThree + byFive


print(divisableNum(15))
