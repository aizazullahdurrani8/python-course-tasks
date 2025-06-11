# Input daily work hours for a week
work_hours = [int(x) for x in input('Enter hours per day in entire week, separated by space: ').split()]

# Input hourly wage
wage = int(input('Enter hourly wage: '))

# Calculate total hours and salary
total = sum(work_hours)
salary = total * wage

# Display result
print('Salary is', salary)