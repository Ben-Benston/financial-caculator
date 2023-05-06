import sys
import datetime
import random

global principalAmt
global ratInt
global month

def priAmt():
    global principalAmt
    principalAmt = input("\nPlease enter the Principal Amount : ")
    try:
        (float(principalAmt))
    except:
        priAmt()
    principalAmt = (float(principalAmt))

def intAmt():
    global ratInt
    ratInt = input("Please enter the rate of interest in % : ")
    try:
        (float(ratInt)/100) 
    except:
        intAmt()
    ratInt = (float(ratInt)/100)

def months():
    global month
    month =  input("Please enter the number of months / years : ")
    try:
        (float(month))
    except:
        months()
    month = (float(month))

def simpInt():
    print("\nCalculating Simple Interest ----")
    priAmt()
    intAmt()
    months()

    simp = (principalAmt*ratInt)/12
    simp = str("{:.2f}".format(simp))
    print("\nThe interest per month is " + simp)
    simp = (principalAmt*ratInt)/12*month
    simp = str("{:.2f}".format(simp))
    print("The total interest in " + str(month) + " months is " + simp)
    simp = principalAmt*ratInt
    simp = str("{:.2f}".format(simp))
    print("\nThe interest per year is " + simp)
    simp = principalAmt*ratInt*month
    simp = str("{:.2f}".format(simp))
    print("The total interest after " + str(month) + " years is " + simp)
    cal()

def compIntAn():
    print("\nCalculating Compound Interest ----")
    priAmt()
    intAmt()
    months() # create a year function and replace with months function

    yeMon = input("Y for Yearly and M for Months : ")
    if yeMon.capitalize() == "Y":
        comp = (principalAmt*(pow((1+ratInt),month))) - principalAmt
        comp = str("{:.2f}".format(comp))
        print("\nThe total compound interest for "+str(month)+" years is " + str(comp))
        comp = principalAmt*pow((1+ratInt),month)
        comp = str("{:.2f}".format(comp))
        print("Future value after "+str(month)+" years is " + str(comp))
    elif yeMon.capitalize() == "M":
        comp = (principalAmt*pow((1+ratInt/12),month)) - principalAmt
        comp = str("{:.2f}".format(comp))
        print("\nThe total compound interest for "+str(month)+" months is " + str(comp))
        comp = (principalAmt*pow((1+ratInt/12),month))
        comp = str("{:.2f}".format(comp))
        print("Future value after "+str(month)+" months is " + str(comp))
    cal()

def loanElig():
    FamInc = input("Please input your family's annual income : ")
    try:
        float(FamInc)
    except:
        loanElig()
    FamInc = float(FamInc)
    print("\nYou can get a loan of approximately ₹" + str(FamInc*0.55) +". This result may vary")
    cal()

def emiCal():
    priAmt()
    intAmt()
    months()

    yeMon = input("Y for Yearly and M for Months : ")
    if yeMon.capitalize() == "M":
        if ratInt == 0:
            emi = principalAmt / month
            emi = str("{:.2f}".format(emi))
            print("\nEMI per month is ₹" + emi)
            emi = (principalAmt/month)*month
            emi = str("{:.2f}".format(emi))
            print("Total EMI for "+str(month) +" months is ₹" + emi)
        else:
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
        cal()
    elif yeMon.capitalize() == "Y":
        if ratInt == 0:
            emi = principalAmt / month
            emi = str("{:.2f}".format(emi))
            print("\nEMI per year is ₹" + emi)
            emi = (principalAmt/month)*month
            emi = str("{:.2f}".format(emi))
            print("Total EMI for "+str(month) +" years is ₹" + emi)
        else:
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
            print("\nInterest per Year is ₹"+emiFull)
            emi = principalAmt*(ratInt)*pow((1+ratInt),month)/(pow((1+ratInt),month)-1)
            emiFull = emi*month-principalAmt
            emiFull = str("{:.2f}".format(emiFull))
            print("Total Interest for " +str(month) +" years is ₹" + emiFull)
    cal()

def sip():
    monthInves = input("Please input your monthly investmest : ")
    try:
        float(monthInves)
    except:
        loanElig()
    monthInves = float(monthInves)

    intAmt()
    months()
    
    investedAmt = monthInves*12*month
    print(investedAmt)# Still in progress
    
def cal():
    inp = input("\n--------------------------------------------------------------------------------\n--Type A for Simple Interest\n--Type B for Compound Interest\n--Type C for loan Eligibility\n--Type D for EMI Calculation\n== ")
    char = list(inp)
    if (len(char)) == 1:
        if str(char[0]).capitalize() == "A":
            simpInt()
        elif char[0].capitalize() == 'B':
            compIntAn()
        elif char[0].capitalize() == 'C':
            loanElig()
        elif char[0].capitalize() == 'D':
            emiCal()
        elif char[0].capitalize() == 'E':
            print("\n\nThe creator of this caculator is Ben Benston.\nFormulas verified by Ah**d Gh****li & Ben Benston.\nHope you have a good day.\nHope I helped you in your calculation :)\n--------------------------------------------------------------------------------") 
            # Names are modified due to privacy reasons.
            sys.exit()
        else:
            cal()
    else: 
        cal()
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
    #70 Different AI Names
currentTime = datetime.datetime.now()
if currentTime.hour < 12:
    print("\n--------------------------------------------------------------------------------\nGood Morning. My name is "+ random.choice(AIname) + "\nI am an AI. I help you to calculate all your math problems. Hope I am correct." )
elif 12 <= currentTime.hour < 18:
    print("\n--------------------------------------------------------------------------------\nGood Afternoon. My name is "+ random.choice(AIname) + "\nI am an AI. I help you to calculate all your math problems. Hope I am correct.")
else:
    print("\n--------------------------------------------------------------------------------\nGood Evening. My name is "+ random.choice(AIname) + "\nI am an AI. I help you to calculate all your math problems. Hope I am correct.")

cal()
