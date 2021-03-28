#  Coding a function that prints the highest even number from a list

#Two Ways:

#1
list1= [10,2,4,6,7,8,9,3,11]

def highest_even(list):
  even_li=[]
  for num in list:
    if num % 2 == 0:
      even_li.append(num)
  li = sorted(even_li)
  return li[-1]

print(highest_even(list1))

#Or can use the 'max' function instead of sorting the list, and can list the numbers in the argument itself:
#2

def highest_even_nu(list):
  even_nu=[]
  for num in list:
    if num % 2 == 0:
      even_nu.append(num)
  return (max(even_nu))

print(highest_even_nu([10,2,4,6,7,8,9,3,11]))