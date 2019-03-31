def my_func(x):
	return x

# calculating an integral by Simpson's method
def simpsonIntegr(a, b, func, stepcnt=41):
	if(stepcnt and stepcnt%2 == 1):
		step = (b-a)/(stepcnt-1)
		ret = func(a) + func(b)

		for i in range(1, stepcnt-1):
			a += step
			if i%2 == 1:
				ret += 4*func(a)
			else:
				ret += 2*func(a)

		return ret*step/3


if __name__ == "__main__":
	print(simpsonIntegr(0, 5, my_func))
