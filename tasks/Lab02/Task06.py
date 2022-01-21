total = 0
count = 0
average = 0
while True:
    number = input("number = ")
    if number == "done":
        break
    elif number.isdigit():
        number = int(number)
        total += number
        count += 1
        average = total / count
    else:
        print("Invalid input")
    continue

print(f"Total = {total} , Count = {count} , Average = {average}")
