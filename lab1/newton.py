from test_env import fun, validate

def derivative(x, coef_0 = 1, coef_1 = 4.81, coef_2 = -17.37):
	return fun(x, 0, 3*coef_0, 2*coef_1, coef_2)

def second_deriative(x, coef_0 = 1, coef_1 = 4.81, coef_2 = -17.37):
	return fun(x, 0, 0, 6*coef_0, 2*coef_1)

def first_side(a, b):
	if fun(a)*second_deriative(a) > 0:
		return a
	else: return b

def newton(a, b, eps, old_x = 0, i = 0):
	if i == 0:
		x_0 = first_side(a, b)
		old_x = x_0

	if abs(fun(old_x)) <= eps:
		return [old_x, fun(old_x), i]

	x_0 = old_x - (fun(old_x)/derivative(old_x))

	if validate(a, x_0):
		return newton(a, x_0, eps, x_0, i + 1)
	else:
		return newton(x_0, b, eps, x_0, i + 1)