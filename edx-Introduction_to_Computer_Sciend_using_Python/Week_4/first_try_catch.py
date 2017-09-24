try:
	a = int(input())
	b = int(input())
	print(a/b)
	print('ok')
except ValueError:
	print('Você não me ofereceu apenas números')
except ZeroDivisionError:
	print('Você ofereceu um denominador 0')
except:
	print('Algo está errado')
finally:
	print('Outside')
