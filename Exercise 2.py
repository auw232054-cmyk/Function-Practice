#Write a function is_even(number) that returns a Boolean value. Use it to create
#a list of even values from 1 through 20.
even_values=[]
def is_even(number):
      if number%2==0:
          return True
      else:
         return False

even_value=[]
for i in range(1,21):
    if is_even(i):
        even_value.append(i)
print(is_even(9))
print(even_value)
