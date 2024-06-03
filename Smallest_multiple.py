import math
def compute():
	ans = math.lcm(*range(1, 21))
	return str(ans)


if _name_ == "_main_":
	print(compute())
