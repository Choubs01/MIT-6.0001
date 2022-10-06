annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter your semi-annual raise: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04
r1 = r/12 + 1

total_needed_cost = total_cost*portion_down_payment
months = 0

while current_savings < total_needed_cost:
    current_savings = current_savings*r1 + annual_salary*portion_saved/12
    months += 1
    if months % 6 == 0:
        annual_salary = annual_salary*(semi_annual_raise + 1)

print(months)
