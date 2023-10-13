# identifiers (name)

hello = "Alex"
print("Welcome", hello)

# return statement in functions


def mul(a, b):
    return a * b

# calling the mul function but it wont print anything
# mul(4, 5)


print(mul(3, 2))


# GIT (VCS, version control system)
# Github (remote code storing service)

def calculate_mortgage():
    """
    Calculate the monthly mortgage payment based on user inputs.

    Returns:
    float: Monthly mortgage payment.
    """
    # Get user inputs
    loan_amount = float(input("Enter loan amount: $"))
    annual_interest_rate = float(input("Enter annual interest rate (%): "))
    loan_term_years = int(input("Enter loan term in years: "))

    # Convert annual interest rate to decimal form
    monthly_interest_rate = annual_interest_rate / 100 / 12

    # Total number of payments
    total_payments = loan_term_years * 12

    # Calculate monthly payment using the formula
    monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate)
                                     ** total_payments) / ((1 + monthly_interest_rate) ** total_payments - 1)

    return monthly_payment


# Calculate and display the monthly mortgage payment
monthly_payment = calculate_mortgage()
print(f"Monthly mortgage payment: ${monthly_payment:.2f}")
