print("Welcome to the Pattern Generator and Number Analyzer!")
print("\nSelect an option:")
print("1. Generate a Pattern")
print("2. Analyze a Range of Numbers")
print("3. Exit")

option = int(input("Enter your choice :"))

match option:
    case 1:
        print("Genrate a Pattern")
    case 2:
        print("Analyze a Range of Numbers")
    case 3:
        print("Exit")

rows=int(input("please enter the number of rows for the pattern:"))

for i in range(rows):
    for j in range(i + 1): 
        print("*", end=" ")  
    print()

print("\nSelect an option:")
print("1. Generate a Pattern")
print("2. Analyze a Range of Numbers")
print("3. Exit")

option = int(input("Enter your choice :"))
match option:
    case 1:
        print("Genrate a Pattern")
    case 2:
        print("Analyze a Range of Numbers")
    case 3:
        print("Exit")




