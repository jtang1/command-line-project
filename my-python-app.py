import datetime

print("WELCOME TO THE HOUSE PRICE BUDGET CALCULATOR. THIS CALCULATOR WILL TELL YOUR BUDGET FOR BUYING A NEW PROPERTY.\n")

def htb_equity_loan(equity_loan):
    if equity_loan == "Yes" or equity_loan == "yes":
        percentage_gov_own = int(input("What percentage does the government own?: "))
        return True, percentage_gov_own
    if equity_loan == "No" or equity_loan == "no": 
        percentage_gov_own = 0
        return False, percentage_gov_own   

def proceeds_from_sale(loan, sale_price, remaining_mortgage_balance):
    if loan == False:
        proceeds = sale_price - remaining_mortgage_balance
        print("The proceeds from your sale is " + "£" + "{:,.2f}".format(proceeds))
    elif loan == True:
        proceeds = sale_price - remaining_mortgage_balance - ((percentage_gov_own/100) * sale_price)
        print("The proceeds from your sale is " + "£" + "{:,.2f}".format(proceeds))
    return proceeds

def mortgage_borrow_range(no_of_applicants):
    joint_salary = 0
    for each_applicant in range(0, no_of_applicants):
        joint_salary += int(input("Enter the salary of applicant " + str(each_applicant + 1) + ": £"))
    lower_limit = joint_salary * 3.5
    upper_limit = joint_salary * 4
    current_date = datetime.date.today()
    print("Based on the mortgage market at " + str(current_date) + ", the range you can borrow is from £" + "{:,.2f}".format(lower_limit) + " to " + "£" + "{:,.2f}".format(upper_limit) + ".")
    return lower_limit, upper_limit

def budget_calculator(deposit, proceeds, lower_limit, upper_limit):
    budget_lower = deposit + proceeds + lower_limit
    budget_higher = deposit + proceeds + upper_limit
    print("The lower limit of house price you can purchase is " + "£" + "{:,.2f}".format(budget_lower))
    print("The upper limit of house price you can purchase is " + "£" + "{:,.2f}".format(budget_higher))


if __name__ == '__main__':

    loan, percentage_gov_own = htb_equity_loan(input("Do you have a Help to Buy Equity Loan? "))

    sale_price = int(input("Enter the value of your current home: £"))
    remaining_mortgage_balance = int(input("Enter your remaining mortgage balance: £"))

    proceeds = proceeds_from_sale(loan, sale_price, remaining_mortgage_balance)

    lower_limit, upper_limit = mortgage_borrow_range(int(input("How many applicants are applying for this mortgage? ")))

    deposit = int(input("Enter how much you wish to put down as a deposit (excluding the proceeds from the sale): £"))

    budget_calculator(deposit, proceeds, lower_limit, upper_limit)
