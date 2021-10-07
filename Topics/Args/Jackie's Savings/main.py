def final_deposit_amount(*interest_rates, amount=1000):
    current_amount = amount
    for interest_rate in interest_rates:
        interest = (current_amount * interest_rate) / 100
        current_amount += interest
    return round(current_amount, 2)
