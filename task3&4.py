# Task 1 check number is even or odd
num = int(input("Enter The Number to check Even or Odd: "))

if num % 2 == 0:
    print(f"{num} is an Even number")
else:
    print(f"{num} is an Odd number")

# Task 2 For loop using number addition

total = 0
for i in range(1,50):
    total = total+i
print(f"Addition is 1 to 50 : {total}")

