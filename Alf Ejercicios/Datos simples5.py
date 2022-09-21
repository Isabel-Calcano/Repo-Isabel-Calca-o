hours= int(input("How many hours did you work? "))
salary= float(input("What is your hourly rate? "))
print(f"You have worked {hours} hours, for a total of ${round(salary*hours,2)}")