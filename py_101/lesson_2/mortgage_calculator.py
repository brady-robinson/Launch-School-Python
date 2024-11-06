def get_float(prompt):
    while True:
        inp_float = input(prompt)
        try:
            float(inp_float)
            return inp_float
        except ValueError:
            print("Invalid input.")

def format_usd(amount):
    return f"${round(amount, 2):,}"

def calc_monthly_payment(p, j, n):
    """
    p = loan amount
    j = monthly interest rate
    n = loan duration in months
    """
    return p * (j / (1 - (1 + j) ** (-n)))

loan_amount = get_float("What is the loan amount?\n")
loan_amount = float(loan_amount)

apr = get_float("What is the annual APR?\n")
monthly_int_rate = float(apr) / 12
loan_dur_months = get_float("What is the loan duration in months?\n")
loan_dur_months = float(loan_dur_months)

monthly_payment = calc_monthly_payment(loan_amount, monthly_int_rate, loan_dur_months)

print(format_usd(monthly_payment))