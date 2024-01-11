deposited_sum = float(input())
term = float(input())
annual_interest_rate = float(input())

accrued_interest = deposited_sum * (annual_interest_rate / 100)
interest = accrued_interest / 12
total = deposited_sum + (term * interest)
print(total)


#сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)