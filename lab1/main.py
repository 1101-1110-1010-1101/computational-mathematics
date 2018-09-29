import half_div
from test_env import get_keys, build_plot
from termcolor import cprint

keys = get_keys()

if keys.get("--a"):
	a = float(keys.get("--a"))
else:
	print('Введите a:')
	a = float(input())

if keys.get("--b"):
	b = float(keys.get("--b"))
else:
	print('Введите b:')
	b = float(input())

if keys.get("--eps"):
	eps = float(keys.get("--eps"))
else:
	print('Введите eps:')
	eps = float(input())

res = half_div.half(a, b, eps)
print('-------------------------Results-------------------------')
cprint(f"x = {res[0]}, f(x) = {res[1]:.10f}, итераций {res[2]}", 'yellow')
print('---------------------------------------------------------')