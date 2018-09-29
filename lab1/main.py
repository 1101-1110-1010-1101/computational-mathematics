import half_div
import newton
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

half_div_res = half_div.half(a, b, eps)
newton_res = newton.newton(a, b, eps)
print('-------------------------------------Results-------------------------------------')
cprint(f"1. Half dividing: x = {half_div_res[0]}, f(x) = {half_div_res[1]:.10f}, {half_div_res[2]} iterations", 'yellow')
cprint(f"2. Newton: x = {newton_res[0]}, f(x) = {newton_res[1]:.10f}, {newton_res[2]} iterations", 'yellow')
print('---------------------------------------------------------------------------------')