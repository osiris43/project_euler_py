def sum_of_squares(n):
  result = 0

  for x in range(n+1):
    result += x**2 

  return result

def square_of_sum(n):
  result = 0

  for x in range(n+1):
    result += x

  return result**2

if __name__ == '__main__':
  x = sum_of_squares(100)
  y = square_of_sum(100)
  print y - x
