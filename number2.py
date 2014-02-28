lookup_values = {}

def fib(n):
  if lookup_values.has_key(n): return lookup_values[n]

  if n < 2: 
    lookup_values[n] = 1
    return 1 
  else:
    lookup_values[n] = fib(n-1) + fib(n-2)
    return lookup_values[n]

def build_fib_list(n):
  fiblist = []
  for x in range(n):
    y = fib(x)
    if y > 4000000: break

    print y
    if y % 2 == 0: fiblist.append(y)

  return fiblist

if __name__ == '__main__':
  fiblist = build_fib_list(1000)
  print fiblist
  print reduce(lambda x, y: x + y, fiblist)
  
