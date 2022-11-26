def fib(num):
  """
  Finds nth fibonacci number
  :param num: An integer number
  :return: nth fibonacci number
  """
  # Base Case
  if num <= 1:
    return num

  second_last = 0  # The 0th 
  last = 1  # The first  
  current = 0

  for i in range(2, num + 1):
    # current is the sum of the last plus second last number before the current one
    current, second_last = second_last + last, last
    last = current

  return current

# Driver code to test above function
if __name__ == '__main__':
  num = 6
  print(fib(num))
