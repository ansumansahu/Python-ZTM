class Toy():
  def __init__(self, color, age):
    self.color = color
    self.age = age
    self.my_dict = {
        'name':'Ansh',
        'has_toys': False,
    }

  def __str__(self):
    return f"{self.color}"

  def __len__(self):
    return 5

  def __del__(self):
    return "deleted"

  def __call__(self):
      return('yes??')

  def __getitem__(self,i):
      return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
#both syntax give same output
print(str('action_figure'))
#str is only modified for this specific object as we modified 
#the dunder method but otherwise it does what it's meant for

print(len(action_figure)) #same like str

print(action_figure())
#here we use call method
#this is same as action_figure.__call__()
print(action_figure['name'])
print(action_figure.__getitem__('name'))