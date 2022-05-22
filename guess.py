import random

start = input('請決定隨機數字範圍開始值:')
end = input('請決定隨機數字範圍結束值:')
start = int(start)
end = int(end)

r = random.randint(start,end) #random interger 有包含一盒一百
count = 0
while True:
	count = count + 1  #count +=1 也可
	num =input('請猜猜看數字:')
	num = int(num)
	if num == r:
		print('終於猜對了')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('你猜錯了,答案比你猜的數小')
	elif num < r:
		print('你猜錯了,答案比你猜的數大')	
	print('這是你猜的第', count, '次')