#wap take emp salary from keyboard if sal>=5000 da=30% hra=20% then display basic entry da hra and total
salary =int(input("Enter Basic Salary: "))
da = 0
hra = 0
if salary >= 5000:
    da = salary * 0.30
    hra = salary * 0.20
total = salary + da + hra
print("\nBasic Salary =", salary)
print("DA =", da)
print("HRA =", hra)
print("Total Salary =", total)