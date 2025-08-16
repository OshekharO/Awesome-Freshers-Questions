numbersEntered = []
lengthNumbers = int(input("Please enter the length of your list/array: "))
print("Please enter your numbers individually: ")

for x in range(lengthNumbers):
    data = int(input())
    if data == -1000:
        print("-1000 received, exiting")
        exit()
    numbersEntered.append(data)

def menu():
    print("[A] Smallest")
    print("[B] Largest")
    print("[C] Quit")

menu()

while True:
    option = input("Please select either option A,B,or C: ")
    if option == "A":
        print("The smallest number is:", min(numbersEntered))
    elif option == "B":
        print("The largest number is:", max(numbersEntered))
    elif option == "C":
        print("Quit")
        break
