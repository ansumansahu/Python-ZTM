from collections import Counter,defaultdict
import datetime
from typing import DefaultDict
#Counter,OrderedDict are classes 

li=[1,2,3,4,5,6,3,4]
sentence='useful modules'
print(Counter(li))
print(Counter(sentence))
#creates dictionary(or hashmap) keeping track how many items item occured

my_dict=DefaultDict(bool,{'a':1,'b':2})
print(my_dict['a'])
print(my_dict['c'])

from datetime import time,date
print(time(10,10,00))
print(date.today())

from array import array
arr=array('i',[1,2,3,4])
print(arr)
print(arr[1])