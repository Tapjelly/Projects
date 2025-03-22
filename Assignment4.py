accounts = {1234: 1000, 1111: 500}


def login(x):
    for key in accounts:
        if x == key:
            return True


def menu():
    menuSelection = int(input("\nPlease Press 1 For Your Balance\n"
                              "Please Press 2 To Make a Withdrawl\n"
                              "Please Press 3 To Pay in\n"
                              "Please Press 4 To Return Card\n"
                              "What Would you like to choose?"))
    return menuSelection


def withdrawMenu():
    menuOptions = int(input("\nHow much would you like to withdraw?"
                            "\n$10\n$20\n$40\n$60\n$80\n$100\n"
                            "For other enter 1: "))
    if menuOptions == 1:
        menuOptions = int(input("Please enter desired amount: "))
    return menuOptions


def withdraw(x, y):
    if x >= y:
        return x - y
    else:
        print("Insufficient Funds")


print("Welcome to Humber Bank ATM")
tries = 0
cont = True
while cont:
    if tries == 3:
        print("No more tries")
        break
    try:
        pin = int(input("Please Enter Your 4 Digit Pin:"))
        if not login(pin):
            print("Incorrect Password")
            tries += 1

        while login(pin):
            choice = menu()
            try:
                if choice == 1:
                    print("\nYour Balance is: " + str(accounts[pin]))
                    question = input("\nWould you like to go back? y/n: ")
                    if question == "n":
                        print("Thank You")
                        break

                elif choice == 2:
                    menuOptions = int(input("\nHow much would you like to withdraw?"
                                            "\n$10\n$20\n$40\n$60\n$80\n$100\n"
                                            "For other enter 1: "))
                    if menuOptions == 1 or menuOptions == 10 or menuOptions == 20 or menuOptions == 40 or menuOptions == 60 or menuOptions == 80 or menuOptions == 100:
                        if menuOptions == 1:
                            menuOptions = int(input("Please enter desired amount: "))
                        amount = menuOptions
                    newAmount = withdraw(accounts[pin], amount)
                    accounts[pin] = newAmount
                    print("\nYour New Balance is: " + str(accounts[pin]))
                    question = input("\nWould you like to go back? y/n: ")
                    if question == "n":
                        print("Thank You")
                        break

                elif choice == 3:
                    amount = int(input("\nHow much Would You Like To Deposit? "))
                    accounts[pin] += amount
                    print("Your New Balance is: " + str(accounts[pin]))
                    question = input("\nWould you like to go back? y/n: ")
                    if question == "n":
                        print("Thank You")
                        break

                elif choice == 4:
                    print("Thank You\n")
                    pin = False
                else:
                    print("Invalid Menu Selection")
            except NameError:
                print("Error, Invalid input")
    except ValueError:
        print("Error, Invalid input")
