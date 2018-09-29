def fun(x, coef_0 = 1, coef_1 = 4.81, coef_2 = -17.37, coef_3 = 5.38):
	return (coef_0 * x**3) + (coef_1 * x**2) + (coef_2 * x) + coef_3

def validate(a, b):
  if fun(a)*fun(b) < 0:
    return True
  else: return False

def half(a, b, eps, i = 0):   
  x_0 = (a + b)/2  
  if a < 0 and b > 0:
    l = b + abs(a)
  elif a < 0 and b < 0:
  	l = abs(a) - abs(b)
  else: l = b - a
  if abs(fun(x_0)) <= eps:
    return [x_0, fun(x_0), i]   
  i += 1
  if validate(a, x_0):
    return half(a, x_0, eps, i)
  else:
    return half(x_0, b, eps, i)