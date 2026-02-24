sal=int(input("Enter Basic Salary: "))
da=sal*0.30 if sal>=5000 else sal*0.2
hra=sal*0.20 if sal>=5000 else sal*0.1
total=sal+da+hra
print("Basic Salary =",sal)
print("da =",da)
print("hra =",hra)
print("Total Salary =",total)
