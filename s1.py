def display_student(student_id,name):
    id=input("enter id")
    print(f"student id : {student_id}")
    print(f"student name : {name}")

def calculate_total(mark1,mark2,mark3,mark4,mark5):
    total=mark1+mark2+mark3+mark4+mark5
    percentage=(total/500)*100
    print(f"percentage is {percentage}")
    find_grade(percentage)

def find_grade(percentage):
    if 90<=percentage<=100:
        print("Grade A")
    elif 75<=percentage<=89:
        print("Grade B")
    elif 60<=percentage<=74:
        print("Grade C")
    elif 40<=percentage<=59:
        print("Grade D")
    else:
        print("Fail")

def highest_mark(mark1,mark2,mark3,mark4,mark5):
    mark=[mark1,mark2,mark3,mark4,mark5]
    highest=mark[0]
    for i in mark:
        if i>highest:
            highest=i
    print(f"highest marks among all subjects is : {highest}")

def lowest_mark(mark1,mark2,mark3,mark4,mark5):
    mark=[mark1,mark2,mark3,mark4,mark5]
    lowest=mark[0]
    for j in mark:
        if j<lowest:
            lowest=j
    print(f"lowest marks among all subjects is : {lowest}")

def pass_fail(mark1,mark2,mark3,mark4,mark5):
    mark=[mark1,mark2,mark3,mark4,mark5]
    for i in mark:
        if i<35:
            print("fail")
    else:
        print("pass")

def main():
    display_student(101,'rahul')
    calculate_total(90,85,95,78,88)
    highest_mark(90,85,95,78,88)
    lowest_mark(90,85,95,78,88)
    pass_fail(90,85,95,78,88)

main()