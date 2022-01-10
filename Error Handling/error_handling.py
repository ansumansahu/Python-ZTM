#Suppose we want to print age by input
# age=input('Enter age: ')
# print(age)

#Works fine but we can also give random string inputs
#How to avoid?

age=int(input('Enter age: '))
print(age)

#But while programming we want to avoid getting errors
#So what we should do is- Error Handling
while True:
    try:
        score=int(input('Enter score: '))
        print(100/score)
    except ValueError:
        print('Score should be a integer')
    except ZeroDivisionError:
        print('Score cannot be zero')
    else:
        break
