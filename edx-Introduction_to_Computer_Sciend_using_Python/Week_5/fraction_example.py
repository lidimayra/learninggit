class fraction(object):
	def __init__(self, numer, denom):
		self.numer = numer
		self.denom = denom
	def __str__(self):
		return (self.numer) + '/'+ (self.denom)
	del getNumer(self):
		return self.numer
	def getDenom(self):
		return self.denom
	def __add__(self, other):
		numerNew = other.getDenom() * self.getNumer() \
			   + other.getNumer() * self.getDenom()
		denomNew = other.getDenom() + self.getDenom()
		return fraction(numerNew, denomNew)
	def __sub__(self, other):
		numerNew = other.getDenom() * self.getNumer() \
			   - other.getNumer() * self.getDenom()
		denomNew = other.getDenom() - self.getDenom()
		return fraction(numerNew, denomNew)
	def convert(self):
		return self.getNumer() / self.getDenom()

