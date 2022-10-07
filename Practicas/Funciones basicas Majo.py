def sumar():
    result= num1 + num2
    rounded_result= round(result,2)
    print(rounded_result)

    return "Thanks for using the 'Too simple calculator'"

num1 = float(input("please write a number: "))
num2 = float(input("please write another number: "))

print(sumar())