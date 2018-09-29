from test_env import fun, validate

def half(a, b, eps, i = 0):   
  x_0 = (a + b)/2  
  if a < 0 and b > 0:
    l = b + abs(a)
  elif a < 0 and b < 0:
  	l = abs(a) - abs(b)
  else: l = b - a
  if abs(fun(x_0)) <= eps:
    return [x_0, fun(x_0), i]
  if validate(a, x_0):
    return half(a, x_0, eps, i + 1)
  else:
    return half(x_0, b, eps, i + 1)