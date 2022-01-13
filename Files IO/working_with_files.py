with open('Sample_text.txt', mode='r+') as my_file:
    text=my_file.write('Hey we are reading this file as of now')
    print(text)

#Mode r+ means read and write
#Mode append adds text to end 
#we can actually create file with mode set to w
with open('Sample_text2.txt', mode='w') as my_file:
    text=my_file.write('This file was not originally present')
    print(text)

