#Prints how many months it would take to save up for an intended amount according to salary and saving goal inputs, and other factors
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04
r1 = r/12 + 1

monthly_salary = annual_salary*portion_saved/12
total_needed_cost = total_cost*portion_down_payment
months = 0

while current_savings < total_needed_cost:
    current_savings = current_savings*r1 + monthly_salary
    months += 1

print(months)
