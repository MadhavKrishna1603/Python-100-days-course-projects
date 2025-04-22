def calculator(firstnumber,operation_,secondnumber,):
    ans_ = 0
    if operation_ == "+":
        add(firstnumber,secondnumber)
        # print(f"{firstnumber} {operation} {secondnumber} = {add(firstnumber,secondnumber)}")
        ans_ += add(firstnumber,secondnumber)
        return ans_
    elif operation_ == "-":
        subtract(firstnumber,secondnumber)
        # print(f"{firstnumber} {operation} {secondnumber} = {subtract(firstnumber, secondnumber)}")
        ans_ += subtract(firstnumber, secondnumber)
        return ans_
    elif operation_ == "*":
        multiply(firstnumber,secondnumber)
        # print(f"{firstnumber} {operation} {secondnumber} = {multiply(firstnumber, secondnumber)}")
        ans_ += multiply(firstnumber, secondnumber)
        return ans_
    elif operation_ == "/":
        divide(firstnumber,secondnumber)
        # print(f"{firstnumber} {operation} {secondnumber} = {divide(firstnumber, secondnumber)}")
        ans_ += divide(firstnumber, secondnumber)
        return ans_
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operators ={"+" : add ,
             "-" : subtract ,
             "*" : multiply ,
             "/" : divide}
tom = True
while tom :
    to_continue="y"
    first_number = float(input("What is the first number: "))
    while(to_continue=="y"):
        operation = input("+\n-\n*\n/\nPick an operation?: ")
        second_number = float(input("Enter the next number?: "))
        print(f"{first_number} {operation} {second_number} = {calculator(first_number,operation,second_number)}")
        rerun = input(f"Type 'y' to continue calculating with the {calculator(first_number,operation,second_number)} or type 'n' to start a new calculation").lower()5
        to_continue = rerun
        first_number=calculator(first_number,operation,second_number)

    print("\n" * 1000)
