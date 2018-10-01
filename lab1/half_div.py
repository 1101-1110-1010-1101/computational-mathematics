from test_env import fun, validate, interval_len

def half(a, b, eps, i = 1, iter_meta = [["i", "a", "b", "x", "f(a)", "f(b)", "f(x)", "len"]]):
  x_0 = (a + b)/2

  l = interval_len(a, b)

  iter_meta.append([i, a, b, x_0, fun(a), fun(b), fun(x_0), l])

  if abs(fun(x_0)) <= eps:
    return [x_0, fun(x_0), i, iter_meta]

  if validate(a, x_0):
    return half(a, x_0, eps, i + 1, iter_meta)
  else:
    return half(x_0, b, eps, i + 1, iter_meta)