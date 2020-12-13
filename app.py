emp_file = open('employees.txt')

print(emp_file.readable())
#print(emp_file.read()) #reads whole file
print(emp_file.readline())
print(emp_file.readline())

#print(emp_file.readlines())   #reads each line as list

for employee in emp_file.readlines(): #two lines already read
    print("Lines: "+employee)
emp_file.close()
