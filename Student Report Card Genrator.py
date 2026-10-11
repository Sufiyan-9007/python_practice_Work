Name = "Sufiyan Qureshi"
Roll_Number = 1045
Course = "data science"
Marks = [87, 76, 92, 68, 81]

Name = Name.strip()
Name = Name.title()
Course = Course.title()
total=sum(Marks)

print(f'*'*10, "STUDENT REPORT CARD,"*1, f'*'*10)
print(f'{"Name":<20}:{Name.upper()}')
print(f'{"Roll Number":<20}: {Roll_Number}')
print(f'{"Course":<20}: {Course.capitalize()}')
print(f"-"*40)
print(f'{"total Marks":<20}: {total}')
print(f'{"Average Marks":<20}: {total/len(Marks):.2f}')# this line written by using AI