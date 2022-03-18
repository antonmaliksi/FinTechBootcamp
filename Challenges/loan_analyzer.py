# Import necessary Libraries and Paths
import csv
from pathlib import Path

# Part 1
print("Part 1")

# Create a List of loans
loan_costs = [500, 600, 200, 1000, 450]

# Find the number of loans in our List
print(f"The total number of loans (amount) is {len(loan_costs)}")

# Find the total value (sum) of loans in our List
print(f"The total value (sum) of the loans is ${sum(loan_costs)}")

# Find the average loan price in our List
print(f"The average loan price is ${sum(loan_costs) / len(loan_costs)}")


# Part 2
print("Part 2")

# Calculate the Present Value of the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Using .get() on the dictionary above, extract the Future Value and Remaining Months on the loan, then print each variable
# Use the formula for Present Value (monthly) to calculate a "fair value" of the loan
# Use a minimum required return of 20% (or 0.2) as the annual discount rate
future_value = loan.get("future_value")
print(f"The future value is ${future_value}")

remaining_months = loan.get("remaining_months")
print(f"The amount of months remaining is {remaining_months}")

fair_value = loan.get("loan_price")
print(f"The fair value of the loan is ${fair_value}")

annual_discount_rate = 0.2

present_value = future_value / (1+(annual_discount_rate/12)) ** remaining_months

# Write a conditional statement to decide if the present value represents the loan's fair value
# If the present value of the loan is greater than or equal to the cost:
#   Print a message that says the loan is worth at least the cost to buy it
# Else:
#   Print a message that says that the loan is too expensive and not worth the price
if present_value >= fair_value:
    print("The loan is worth at least $500 to buy!")
else: 
    print("The loan is too expensive!")


# Part 3
print("Part 3")

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Define a new function that will be used to calculate present value
# This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
# The function should return the `present_value` for the loan
# Use the function to calculate the present value of the new loan given below
# Use an `annual_discount_rate` of 0.2 for this new loan calculation
future_value = new_loan.get("future_value")
print(f"The future value of the new loan is ${future_value}")

remaining_months = new_loan.get("remaining_months")
print(f"The amount of months remaining on the new loan is {remaining_months}")

annual_discount_rate = 0.2

present_value = future_value / (1+(annual_discount_rate/12)) ** remaining_months

print(f"The present value of the new loan is ${present_value:.2f}")


# Part 4
print("Part 4")

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an empty list called `inexpensive_loans`
inexpensive_loans=[]

# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for cost in loans:
    if cost["loan_price"] <= 500.0:
       inexpensive_loans.append(cost)
    
# Print the `inexpensive_loans` list
print(f"The most inexpsensive loans are {inexpensive_loans}")


# Part 5

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Use the csv library and `csv.writer` to write the header row and each row of `loan.values()` from the `inexpensive_loans` list

csvpath = Path("inexpensive_loans.csv")
with open(csvpath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for row in inexpensive_loans:
        csvwriter.writerow(row.values())