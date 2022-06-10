##coin counter

def quarters(amount):
    quarters = amount/0.25
    answer = str(round(quarters,2))
    print("It takes "+answer+ " quarters")

def nickels(amount2):
    nickels = amount2/0.05
    print("It takes " , nickels, " nickels")

def pennies(amount3):
    pennies = amount3/0.01
    print("It takes " ,pennies , "pennies")
    
def dimes(amount4):
    dimes = amount4/0.10
    print("It takes" , dimes, "dimes")

def main():
    x = int(input("Please enter your whole dollar amount:"))
    quarters(x)
    nickels(x)
    pennies(x)
    dimes(x)

main()
