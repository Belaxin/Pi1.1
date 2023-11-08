def calc():
    Number1 = int(input("Enter number 1 "))
    Operation = input("Which operation? ")
    Number2 = int(input("Enter number 2 "))
    if Operation.__eq__("/"):
        print(Number1 / Number2)

        calc()
    else:
        if Operation.__eq__("*"):
            print(Number1 * Number2)
            calc()
        else:
            if Operation.__eq__("-"):
                print(Number1 - Number2)
                calc()
            else:
                if Operation.__eq__("+"):
                    print(Number1 + Number2)
                    calc()
                else:
                    print("I didn't quite catch that")
                    calc()


calc()

