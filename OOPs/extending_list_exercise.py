class SuperList(list):
    def __len__(self):
        return 1000

super_list1=SuperList()

print(len(super_list1))
super_list1.append(5)
#we can access all methods of list datatype by inheritance
#simply make list parent class of superlist
print(super_list1[0])