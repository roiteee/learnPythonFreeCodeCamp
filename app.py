employee_file = open('employees.txt','a') #appends at the end of file

employee_file.write("Toby - Human Resources")
employee_file.write("\nKelly - Customer Services")  #\n puts next line
employee_file.close()

employee_file = open('employees.txt', 'w') #overrites the file
employee_file.write("Rick - Salesman")
employee_file.close()
