from math import pi, tan

def polysum(n, s):
    	'''
	n: number of sides (number)
	s: lenght of the side (number)
	return: a sum rounded to 4 decimal places
	'''
	area = (0.25 * n * (s**2)) / tan(pi / n)
	perimeter = n * s
	return round(area + (perimeter ** 2), 4)

