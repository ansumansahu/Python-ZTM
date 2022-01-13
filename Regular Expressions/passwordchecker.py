#Password Checker:
#Rules applied: Pass word should be
# Must be 8 Char long 
# Contains atleast 1 Capital Letter
# Contains atleast 1 Number
# Contains atleast 1 Special symbol

import re

format=re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$')
test='password'
test2='pasS@2o#1s'

print(format.search(test))
print(format.search(test2))