#ternary operator
#also called conditional expressions

#condition_if_true if condition else condition_if_false

is_friend=True
can_message='message allowed' if is_friend else "not allowed to message"
print(can_message)

#short circuiting 
#basically putting or in condition (bruh)
is_coder=False
if is_friend or is_coder :
  print("besties")

#name is called so because python interpreter doesn't bother to check
#the second condition as soon as it finds the first condition is "True"