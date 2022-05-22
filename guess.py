import random

r = random.randint(1,100) #random interger 有包含一盒一百
while True:
	num =input('請猜猜看數字:')
	num = int(num)
	if num == r:
		print('終於猜對了')
		break
	elif num > r:
		print('你猜錯了,答案比你猜的數小')
	elif num < r:
		print('你猜錯了,答案比你猜的數大')	