def div(num1,num2):
    try:
        return num1/num2
    except (ZeroDivisionError,ValueError,TypeError) as error:
        return error

# print(div('1',2))
# print(div(1,0))