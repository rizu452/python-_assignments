# Question 1: Count Valid Ages
# Use:
# • while loop
# • continue
# • User input
# Task:
# Keep accepting ages until the user enters -1.
# Ignore ages below 1 and above 120.
# Count valid ages only.
# Example
# Input:
# 25
# 150
# 40
# -5
# 18
# -1
# Output:
# Valid ages count: 3

ages=int(input("enter number of ages:"))
n=0
count=0
while n<ages:
    age=int(input("enter age :"))
    if age>=0 and age<120:
        count+=1
    elif age<=0 and age>=120:
        continue
    n+=1
print("Valid ages count:",count)



# Question 2: Sum Multiples of 5
# Use:
# • while loop
# • continue
# • Modulus operator (%)
# • User input
# Task:
# Keep accepting numbers until the user enters 0.
# Add only numbers divisible by 5.
# Skip all other numbers using continue.
# Example
# Input:
# 10
# 12
# 15
# 18
# 20
# 0
# Output:
# Sum: 45

numbers=int(input("enter numbers:"))
sum=0
n=1
while n>0:
    numbers=int(input("enter numbers:"))
    if numbers<=0:
        break
    elif numbers%5!=0:
        continue
    elif numbers%5==0:
        sum+=numbers
    n+=1
print("sum=",sum)


# Question 3: Count Uppercase Letters

# Use:
# • for loop
# • continue
# • Character comparison
# Task:
# Given:
# text = "PyTHon ProGRAM"
# Count how many uppercase letters are present.
# Skip all other characters using continue.
# Expected Output:
# Uppercase letters count: 8

text=input("enter a text")
n=0
count=0
while n<len(text):
    if 'A'<=text[n]<='Z':
        count+=1
    n+=1
print("uppercase=",count)


sales=[500,0,1200,0,700]
amount=0
for sale in sales:
    if sale<=0:
        continue
    else:
        amount+=sale
print('amount = ',amount)