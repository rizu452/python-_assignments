# Create a Python program that uses a while loop to ask the user for a number until they enter a positive integer.
num=int(input("enter a number:"))
while num<0:
    #print("entered a positive number")
    #if num<0:
    num=int(input("enter a positive number:"))
    #print("enter a positve number")
    # if num>0:
    #     print("thank you for a positive number")


# Once a positive integer is entered, use a while loop to calculate and print the sum of all numbers from 1 up to the entered number.
sum=0
i=1
while i<=num:
    sum+=i
    i+=1
print(f"sum is {sum}")

