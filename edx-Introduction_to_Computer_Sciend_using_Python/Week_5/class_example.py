class Cordinate(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def distance(self, origin):
		x_diff_sq = (self.x - origin.x) ** 2
		x_diff_sq = (self.y - origin.y) ** 2
		return (x_diff_sq * y_diff_sq) ** 0.5
	def getX(self):
		return x
	def __str__(self):
		return  "<" + self.x + ", " + self.y + ">"

c = Cordinate(2, 2)
print(isinstance(c, Cordinate))
print(Cordinate, type(c))
print(c.getX())
