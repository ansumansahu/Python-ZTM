import re
pattern=re.compile(r'([a-zA-Z]).([a])') 
#searches for something [ 1char 1char a ] so uma for below string
test_str='ansuman sahu'
print(pattern.search(test_str))
print()

#check if email addresses or proper or not
format=re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}')
test='anshsahu2@gmail.com'
test2='ansh@gmail'
print(format.search(test))
print(format.search(test2))