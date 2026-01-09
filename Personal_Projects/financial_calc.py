# LD 1st Financial Calculator
import time

# OVERVIEW
# How long it will take to save for a goal based on a weekly or monthly deposit
# Compound Interest Calculator
# Budget Allocator (use set percentages to divide an income into spending categories like savings, entertainment, and food)
# Sale Price Calculator (apply discounts to prices)
# Tip Calculator


# FUNCTIONS

# Saving function: Know whether it is a weekly or monthly deposit. Get user's deposit and what end goal is. calculate
def saving():
    # Get frequency
    while True:
        frec = input("First:\nIs this a WEEKLY or MONTHLY deposit?\n").strip().upper()
        if frec == "WEEKLY":
            # valid input. Break the loop and keep going
            break
        elif frec == "MONTHLY":
            # valid input. Break the loop and keep going
            break
        else:
            print("Please make sure you entered your choice correctly.")
            continue
    # Get how much they are depositing every time
    deposit = float(input("How much are you depositing every time? Omit '$' and commas\n"))
    # Get end goal
    goal = float(input("What is your end goal? Omit '$' and commas\n"))

    def calculate():
        nonlocal deposit
        nonlocal goal
        time = goal / deposit
        return time
    time = calculate()

    if frec == "WEEKLY":
        # Tell how many weeks
        print(f"It will take you {time} weeks to save ${goal} with a weekly deposit of ${deposit}")
    elif frec == "MONTHLY":
        # Tell how many months
        print(f"It will take you {time} months to save ${goal} with a monthly deposit of ${deposit}")
    else:
        # Something went terribly worng. how did this happen
        print("What in God's name did you do to my code?")

# Compound intrest: Get starting amount, intrest rate, and how long it is being left in for. Tell them what the amount would be at the end of that time

# Budget allocator: Get user's catigories and percent for each one, as well as salary. Make sure percents are exactly 100. divide salary into different catigories then tell the user what the math results are

# Sale price: Get BASE ORIGINAL price and the discount. tell user new price

# Tip: Get the amount and how much of a tip they want to leave. Tell user tip amount and what the final total would then be

# Greet: Greet the user and have a menu corresponding to the different calculations that could be done
def greet():
    name = input("Welcome! Before continuing, what is your name?\n").strip().title()
    while True:
        time.sleep(2)
        print(f"\nWelcome {name}! What kind of calculation would you like to preform?")
        print("(1) Time for a Saving Goal\n(2) Calculate Compound Intrest on a Deposit\n(3) Budget based on Salary\n(4) Calculate Price for an Item on Sale\n(5) Calculate a Tip to Leave\n(6) Leave Program")
        choice = int(input("Enter the number corresponding to what you want to do.\n"))
        if choice == 1:
            saving()
        elif choice == 2:
            # call coumpond intrest
            pass
        elif choice == 3:
            # call budget
            pass
        elif choice == 4:
            # call sale
            pass
        elif choice == 5:
            # call tip
            pass
        elif choice == 6:
            # user is leaving
            print("Hope this was helpful for your calculations!\nGoodbye!")
            break
        else:
            print("That doesn't seem to be a valid input. Please try again.")
            continue

greet()