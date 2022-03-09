from multiprocessing.sharedctypes import Value


def collatz(number):
  try:
    while number != 1:
      print(number)
      if (number % 2) == 0:
        number = number // 2
      else:
        number = 3 * number + 1
    print(number)
  except TypeError:
    print('You must enter an interger')


collatz(38)