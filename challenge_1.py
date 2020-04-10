'''Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird'''

def start():
    while True:
        try:
            number = int(input("Enter a integer please: "))
            if number < 0:
                print("Negative integers are not valid, try again")
            else:
                break
        except Exception as e:
                print("Exception occurred: {}".format(e))

    if number%2 > 0:
        print("Weird")
    elif number%2 == 0:
        if number >= 2 and number <= 5:
            print("Not weird")
        elif number >=6 and number <= 20:
            print("Weird")
        elif number > 20:
            print("Not weird")
    else:
        input("something is wrong with your number, try again")

if __name__ == "__main__":
    start()
