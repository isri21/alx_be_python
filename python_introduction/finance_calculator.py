income = int(input("Enter your monthly income: "))
expense = int(input("Enter your total monthly expenses: "))
saving = income - expense
p_saving = int((saving * 12) + (saving * 12 * 0.05))
print(f"Your monthly savings are ${saving}.")
print(f"Projected savings after one year, with interest, is: ${p_saving}.")
