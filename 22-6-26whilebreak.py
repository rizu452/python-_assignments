# Create a simple program that uses a while loop to iterate over a range of numbers from 1 to 10.

num=1
while num<=10:                  # while repeats the loop until it becomes 10 and stops if greateter than 10          
    # print(num)
    num+=1

# Implement a condition to print only the even numbers within this range using the continue statement.

    if num%2!=0:
        continue                #skips that particular statement and continue the loop
    # print(num)

# Add another condition that stops the loop when it encounters the number 8, utilizing the break statement.

    if num==8:
        break                   #stops looping when condition meets
    print(num)

# Ensure your program includes comments explaining the purpose of each segment, especially where break and continue are used.


# Execute your program and document the output to verify it meets the expected behavior.
