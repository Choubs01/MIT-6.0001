annual_salary = float(input("Enter your annual salary: "))
total_cost = 1000000
semi_annual_raise = 0.07
c = annual_salary

portion_down_payment = 0.25
current_savings = 0
r = 0.04
r1 = r/12 + 1
total_needed_cost = total_cost*portion_down_payment

bisection_count = 0
portion_saved = 0.5
months = 0

if annual_salary*3 < total_needed_cost:
    print("Impossible")
    quit()

while True:
    current_savings = current_savings*r1 + annual_salary*portion_saved/12
    months += 1
    if months % 6 == 0:
        annual_salary = annual_salary*(semi_annual_raise + 1)
    if current_savings > total_needed_cost + 100:
        previous_portion_saved = portion_saved
        portion_saved = portion_saved/2
        months = 0
        current_savings = 0
        annual_salary = c
        bisection_count += 1
        continue
    elif months == 36 and current_savings < total_needed_cost - 100:
        portion_saved = (portion_saved + previous_portion_saved)/2
        months = 0
        current_savings = 0
        annual_salary = c
        bisection_count += 1
        continue
    elif months == 36 and  total_needed_cost - 100 <= current_savings <= total_needed_cost + 100:
        portion_saved = portion_saved*100
        print("the optimal savings proportion is " + str(portion_saved) + '%')
        print(bisection_count)
        break
