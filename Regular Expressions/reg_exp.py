#reg expressions are really useful for validation purposes
import re
string='we will seacrch something in this string'
print(re.search('this',string))
#output info - span- (x,y) shows position of searched string
#match object - 'this' - shows the searched string
a= re.search('this',string)
print(a.span())
print(a.start())
print(a.end())

string2='google is great. google helps a lot'
b=re.search('google',string2)
print(b.group())
#group will return string only once even if there are multiple occurences
#returns google only once

#instead of inserting 'item' to search everytime, we can use pattern
string3='ansuman sahu'
pattern=re.compile('s')
a=pattern.search(string3)
print(a)
b=pattern.findall(string3)
print(b)
print(pattern.match(string3))