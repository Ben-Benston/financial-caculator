import sys
import datetime
import random

# Declare global variables for principal amount, interest rate, and number of months/years
global principalAmt
global ratInt
global month

# Function to get and validate the principal amount input from the user
def priAmt():
    global principalAmt
    principalAmt = input("\nPlease enter the Principal Amount : ")
    try:
        (float(principalAmt))
    except:
        # If the input is not a valid float, call the function again to get a new input
        priAmt()
    principalAmt = (float(principalAmt))

# Function to get and validate the interest rate input from the user
def intAmt():
    global ratInt
    ratInt = input("Please enter the rate of interest in % : ")
    try:
        (float(ratInt)/100) 
    except:
        # If the input is not a valid float, call the function again to get a new input
        intAmt()
    ratInt = (float(ratInt)/100)

# Function to get and validate the number of months/years input from the user
def months():
    global month
    month =  input("Please enter the number of months / years : ")
    try:
        (float(month))
    except:
        # If the input is not a valid float, call the function again to get a new input
        months()
    month = (float(month))

# Function to calculate simple interest
def simpInt():
    print("\nCalculating Simple Interest ----")
    # Get principal amount, interest rate, and number of months/years from user
    priAmt()
    intAmt()
    months()

    # Calculate and display interest per month
    simp = (principalAmt*ratInt)/12
    simp = str("{:.2f}".format(simp))
    print("\nThe interest per month is " + simp)

    # Calculate and display total interest for the given number of months
    simp = (principalAmt*ratInt)/12*month
    simp = str("{:.2f}".format(simp))
    print("The total interest in " + str(month) + " months is " + simp)

    # Calculate and display interest per year
    simp = principalAmt*ratInt
    simp = str("{:.2f}".format(simp))
    print("\nThe interest per year is " + simp)

    # Calculate and display total interest for the given number of years
    simp = principalAmt*ratInt*month
    simp = str("{:.2f}".format(simp))
    print("The total interest after " + str(month) + " years is " + simp)

    # Call the main function to continue the program
    cal()

# Function to calculate compound interest
def compIntAn():
    print("\nCalculating Compound Interest ----")
    # Get principal amount, interest rate, and number of months/years from user
    priAmt()
    intAmt()
    months()

    # Ask user if they want to calculate interest yearly or monthly
    yeMon = input("Y for Yearly and M for Months : ")
    if yeMon.capitalize() == "Y":
        # Calculate and display total compound interest for the given number of years
        comp = (principalAmt*(pow((1+ratInt),month))) - principalAmt
        comp = str("{:.2f}".format(comp))
        print("\nThe total compound interest for "+str(month)+" years is " + str(comp))

        # Calculate and display future value after the given number of years
        comp = principalAmt*pow((1+ratInt),month)
        comp = str("{:.2f}".format(comp))
        print("Future value after "+str(month)+" years is " + str(comp))
    elif yeMon.capitalize() == "M":
        # Calculate and display total compound interest for the given number of months
        comp = (principalAmt*pow((1+ratInt/12),month)) - principalAmt
        comp = str("{:.2f}".format(comp))
        print("\nThe total compound interest for "+str(month)+" months is " + str(comp))

        # Calculate and display future value after the given number of months
        comp = (principalAmt*pow((1+ratInt/12),month))
        comp = str("{:.2f}".format(comp))
        print("Future value after "+str(month)+" months is " + str(comp))

    # Call the main function to continue the program
    cal()

# Function to calculate loan eligibility based on family income
def loanElig():
    FamInc = input("Please input your family's annual income : ")
    try:
        float(FamInc)
    except:
        # If input is not a valid float value, call the function again
        loanElig()
    FamInc = float(FamInc)
    # Calculate loan amount as 55% of family income
    print("\nYou can get a loan of approximately ₹" + str(FamInc*0.55) +". This result may vary")
    # Call the main function
    cal()

# Function to calculate EMI for a loan
def emiCal():
    # Call functions to get principal amount, interest rate, and loan duration
    priAmt()
    intAmt()
    months()

    # Ask user if they want EMI calculated on a monthly or yearly basis
    yeMon = input("Y for Yearly and M for Months : ")
    if yeMon.capitalize() == "M":
        if ratInt == 0:
            # If interest rate is 0, calculate EMI and total EMI
            emi = principalAmt / month
            emi = str("{:.2f}".format(emi))
            print("\nEMI per month is ₹" + emi)
            emi = (principalAmt/month)*month
            emi = str("{:.2f}".format(emi))
            print("Total EMI for "+str(month) +" months is ₹" + emi)
        else:
            # If interest rate is not 0, calculate EMI, total EMI, interest per month, and total interest
            emi = principalAmt*(ratInt/12)*pow((1+ratInt/12),month)/(pow((1+ratInt/12),month)-1)
            emi = str("{:.2f}".format(emi))
            print("\nEMI per month is ₹" + emi)
            emi = principalAmt*(ratInt/12)*pow((1+ratInt/12),month)/(pow((1+ratInt/12),month)-1)
            emi = emi * month
            emi = str("{:.2f}".format(emi))
            print("Total EMI for " +str(month) +" months is ₹" + emi)
            emi = principalAmt*(ratInt/12)*pow((1+ratInt/12),month)/(pow((1+ratInt/12),month)-1)
            emiFull = (emi*month-principalAmt)/month
            emiFull = str("{:.2f}".format(emiFull))
            print("\nInterest per Month is ₹"+emiFull)
            emi = principalAmt*(ratInt/12)*pow((1+ratInt/12),month)/(pow((1+ratInt/12),month)-1)
            emiFull = emi*month-principalAmt
            emiFull = str("{:.2f}".format(emiFull))
            print("Total Interest for " +str(month) +" months is ₹" + emiFull)
        # Call the main function
        cal()
    elif yeMon.capitalize() == "Y":
        if ratInt == 0:
            # If interest rate is 0, calculate EMI and total EMI
            emi = principalAmt / month
            emi = str("{:.2f}".format(emi))
            print("\nEMI per year is ₹" + emi)
            emi = (principalAmt/month)*month
            emi = str("{:.2f}".format(emi))
            print("Total EMI for "+str(month) +" years is ₹" + emi)
        else:
            # If interest rate is not 0, calculate EMI, total EMI, interest per year, and total interest
            emi = principalAmt*(ratInt)*pow((1+ratInt),month)/(pow((1+ratInt),month)-1)
            emi = str("{:.2f}".format(emi))
            print("\nEMI per year is ₹" + emi)
            emi = principalAmt*(ratInt)*pow((1+ratInt),month)/(pow((1+ratInt),month)-1)
            emi = emi * month
            emi = str("{:.2f}".format(emi))
            print("Total EMI for " +str(month) +" years is ₹" + emi)
            emi = principalAmt*(ratInt)*pow((1+ratInt),month)/(pow((1+ratInt),month)-1)
            emiFull = (emi*month-principalAmt)/month
            emiFull = str("{:.2f}".format(emiFull))
            print("\nInterest per Year ₹"+emiFull)
            emi = principalAmt*(ratInt)*pow((1+ratInt),month)/(pow((1+ratInt),month)-1)
            emiFull = emi*month-principalAmt
            emiFull = str("{:.2f}".format(emiFull))
            print("Total Interest for " +str(month) +" years is ₹" + emiFull)
        # Call the main function
        cal()
    
# Function to determine which calculation to perform
def cal():
    # Ask user which calculation they want to perform
    inp = input("\n--------------------------------------------------------------------------------\n--Type A for Simple Interest\n--Type B for Compound Interest\n--Type C for loan Eligibility\n--Type D for EMI Calculation\n== ")
    char = list(inp)
    if (len(char)) == 1:
        if str(char[0]).capitalize() == "A":
            # If user chooses A, call the 'simpInt' function
            simpInt()
        elif char[0].capitalize() == 'B':
            # If user chooses B, call the 'compIntAn' function
            compIntAn()
        elif char[0].capitalize() == 'C':
            # If user chooses C, call the 'loanElig' function
            loanElig()
        elif char[0].capitalize() == 'D':
            # If user chooses D, call the 'emiCal' function
            emiCal()
        elif char[0].capitalize() == 'E':
            # If user chooses E, print a message and exit the program
            print("\n\nThe creator of this calculator is Ben Benston.\nFormulas verified by Ah**d Gh****li & Ben Benston.\nHope you have a good day.\nHope I helped you in your calculation :)\n--------------------------------------------------------------------------------") 
            # Names are modified due to privacy reasons.
            sys.exit()
        else:
            # If user inputs an invalid character, call the 'cal' function again
            cal()
    else: 
        # If user inputs more than one character, call the 'cal' function again
        cal()

# List of AI names
AIname = [
        "AC-700", "AC-900", "AF-200", "AJ-700", "AK-700", "AP-400", "AP-700",
        "AV-500", "AX-400", "AX-700", "BL-100", "BV-500", "CX-100", "EM-400",
        "GJ-500", "GS-200", "HK-400", "HR-400", "JB-100", "JB-300", "KL-900",
        "KW-500", "KR-200", "LA-900", "LM-100", "MC-500", "MP-500", "MP-600",
        "MP-800", "PB-600", "PC-200", "PM-700", "PJ-500", "PL-600", "PM-700",
        "QB-100", "RK-200", "RK-800", "RK-900", "RT-600", "RZ-400", "SQ-800",
        "ST-200", "ST-300", "TE-600", "TE-900", "TR-400", "TR-600", "TW-400",
        "VB-800", "VH-500", "VS-400", "VX-500", "WB-200", "WB-400", "WB-500",
        "WD-500", "WE-900", "WF-500", "WG-100", "WG-700", "WJ-700", "WK-500",
        "WM-400", "WM-500", "WR-400", "WR-600", "YK-400", "YK-500", "ZT-200"
    ]

# Get current time
currentTime = datetime.datetime.now()

# Greet user based on current time and print AI name
if currentTime.hour < 12:
    print("\n--------------------------------------------------------------------------------\nGood Morning. My name is "+ random.choice(AIname) + "\nI am a senior software developer. How can I assist you with your calculations today?" )
elif 12 <= currentTime.hour < 18:
    print("\n--------------------------------------------------------------------------------\nGood Afternoon. My name is "+ random.choice(AIname) + "\nI am a senior software developer. How can I assist you with your calculations today?")
else:
    print("\n--------------------------------------------------------------------------------\nGood Evening. My name is "+ random.choice(AIname) + "\nI am a senior software developer. How can I assist you with your calculations today?")

# Call the 'cal' function to start the program
cal()

