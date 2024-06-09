def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def calculation():
    operations={'+':add,'-':subtract,'*':multiply,'/':divide}
    first_num=float(input("Enter the first number: "))
    while(True):
        for key in operations:
            print(key)
        operator=input("choose one of the above operations to be performed: ")
        second_num=float(input("Enter the next number: "))
        result=operations[operator](first_num,second_num)
        print(f"{first_num} {operator} {second_num} = {round(result,2)}")
        repeat = input(f"If you want to continue with {result} enter yes, else enter no to exit the calculator\n or else enter continue to restart the calculator app: ")
        if(repeat=="yes"): 
            first_num=result
        elif(repeat=="continue"):
            calculation()    
        else:
            print("Thanks for using our app")    
            break

calculation()