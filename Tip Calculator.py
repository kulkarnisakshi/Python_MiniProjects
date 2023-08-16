# Tip Calculator 
print("Welcome to the Tip Calculator.")
bill = float(input("What was the total bill ? Rs. "))
tip = int(input("What percentage of tip would you like to give ? "))
tip_calculated = tip / 100
tip_total =  tip_calculated *  bill
total_bill = tip_total + bill
people = int(input("How many people to split the bill ? "))
total = total_bill / people
total_round = round(total,2)
print(f"Each person should pay : Rs. {total_round}")