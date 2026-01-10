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

# Compound intrest: Get starting amount, intrest rate, and how long it is being left in for. Tell them what the amount would be at the end of that time. Equation : final_result = deposit(1+(intrest/12))^(12*years left in)
def compound():
    # Get how much money the user is depositing
    get_money = float(input("How much money are you depositing? Omit '$' and commas.\n"))
    money = round(get_money, 2)
    # Get how many years the user is leaving the money
    get_years = float(input("How many years are you leaving the money in for? Type a number and omit commas.\n"))
    years = round(get_years, 2)
    # Get the intrest rate
    get_intrest = float(input("What is the intrest rate? Enter as a decimal.\n"))
    intrest = round(get_intrest, 2)
    int_intrest = intrest*100

    # Setting up the parts to be used in equation
    def equation():
        fraction = intrest / 12
        roun_frac = round(fraction, 2)
        exponant = 12 * years

        ending_money = money*((1+roun_frac)**exponant)
        rounded_money = round(ending_money, 2)

        return rounded_money
    end = equation()

    # Tell how many weeks
    print(f"If you leave ${money} in for {years} years with an intrest rate of {int_intrest}%, you will have ${end:,}.")
    # Call greet func

# Budget allocator: Get user's catigories and percent for each one, as well as salary. Make sure percents are exactly 100. divide salary into different catigories then tell the user what the math results are
def budget(): # NOT DONE YET
    # Lists for budget catigory and percentage
    catigories = []
    percents = []
    budgets = []
    # Get user's salary
    salary = float(input("What is your monthly salary?\n"))
    # Ask user how many different catigories they want to budget for
    num_of_catigories = int(input("How many catigories do you want to budget for? (Enter whole number)\n"))
    while True:
        # Do a loop based on number of catigories
        for x in range(num_of_catigories):
            catigory = input(f"What is the name of the {x+1} catigory?\n")
            catigories.append(catigory)
        for y in catigories:
            percent = float(input(f"What is the percentage for {y}? Enter as a decimal\n"))
            percents.append(percent)
        # When loop is done, see if all percents are correct (add up to 100)
        total = 0
        for num in percents:
            total += num
        if total == 1:
            # all percents are valid
            break
        else:
            # There must be something wrong with the numbers
            print("It seems like that the percentages you entered don't add to 100%.\nPlease try again.")
            continue
        # if all percents good, leave while loop and start doing the math
    # Get Ms. LaRose's help on being able to work on two lists at once
    # Tell user final results

# Sale price: Get BASE ORIGINAL price and the discount. tell user new price
def onSale():
    og_price = float(input("What is the original price of the item? Omit '$' and commas\n"))
    int_sale = float(input("What is the discount in the item? Omit '%'\n"))
    percent = int_sale / 100

    def subtractDiscount():
        nonlocal og_price
        nonlocal percent

        take_away = og_price * percent
        new_price = og_price - take_away
        return new_price
    discounted = subtractDiscount()
    print(f"The item now costs ${discounted:.2f}")
    # Call greet func

# Tip: Get the amount and how much of a tip they want to leave. Tell user tip amount and what the final total would then be
def leaveTip():
    pass

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