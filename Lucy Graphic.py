Lucy = [
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,0,2,0,0,2,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,2,0,0,2,0,3,3,3,3,0,0,0,0,0],
[0,0,0,0,0,2,2,2,2,0,3,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,3,3,3,3,0,4,0,0,4],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,4],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4]
]

#  The code below prints a graphic of my name

print('Hi I\'m', ('\n'))
for row in Lucy:
  for number in row:
    if number == 0:
      print(' ', end='')
    elif number == 1:
      print('L', end='')
    elif number == 2:
      print('U', end='')
    elif number == 3:
      print('C', end='')
    else:
      print('Y', end='')
  print('')
