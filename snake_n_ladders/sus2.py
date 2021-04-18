def check(y):
	if (y == 485 or y == 375 or y==265 or y ==155 or y==45):
		return True
def check2(y):
	if (y == 430 or y == 320 or y == 210 or y == 100 or y == -10):
		return True

px = {
	1:2,
	2:57,
	3:112,
	4:167,
	5:222,
	6:277,
	7:332,
	8:387,
	9:442,
	10:497
}

ladder = {
	(px[5], 485) : (px[9], 485),
	(px[6], 430) : (px[5], 375),
	(px[3], 430) : (px[1], 100),
	(px[4], 265) : (px[6], 45),
	(px[7], 265) : (px[8], 155),
	(px[3], 155) : (px[3], 100),
	(px[1], 45) : (px[3], -10),
	(px[10], 100) : (px[7], -10)
}

snake = {
	(px[6], 485) : (px[3], 485),
	(px[2], 265) : (px[2], 430),
	(px[8], 430) : (px[10], 210),
	(px[5], 265) : (px[5], 320),
	(px[7], 155) : (px[7], 210),
	(px[3], 45) : (px[2], 155),
	(px[6], 155) : (px[4], -10),
	(px[7], 45) : (px[10], 45)
}

numlist = list(px.keys())
klist_s = list(snake.keys())
vlist_s = list(snake.values())
klist_l = list(ladder.keys())
vlist_l = list(ladder.values())

def cs(x, y):
	for i in range(0, 8):
		q, w = klist_s[i]
		if q==x and w ==y:
			x, y = vlist_s[i]
	return x, y

def cl(x, y):
	for i in range(0, 8):
		q, w = klist_l[i]
		if q==x and w ==y:
			x, y = vlist_l[i]
	return x, y

def check_last_row(x, y, dr):
	for num in range (0, 8):
		if dr >= numlist[num]:
			x = x
			y = y
			print(x, y)

	if dr < (list(px.keys())[list(px.values()).index(x)]):
		print(list(px.keys())[list(px.values()).index(x)])
		print(dr)
		x -= (55*dr)
		y = y
		print(x, y)
	return x, y

w = 55

def impostar(x, y, dr):
	chance = 'po'
	if x == px[1] and y == -10 :
		x = x
		y = y
		print("You won")

	elif x in range(px[1], px[5]) and dr == 6 and check(y):
		print("Q")
		x += (w*dr)
		print("g")
		print(x)
		chance = 'homer'

	elif dr == 6 and check(y):
		print("W")
		chance = 'homer'
		print('here in the awesomeness')
		if x == px[5]:
			x += (w*5)	
			print("a")
			print(x)
		elif x == px[6]:
			x += ((w*4)-(w*(dr-5)))
			print("b")
			print(x)
		elif x == px[7]:
			x += ((w*3)-(w*(dr-4)))
			print("c")
			print(x)
		elif x == px[8]:
			x += ((w*2) - (w*(dr-3)))
			print("d")
			print(x)
		elif x == px[9]:
			x += ((w*1) - (55*(dr-2)))
			print("e")
			print(x)
		elif x == px[10]:
			x -=(w*(dr-1))
			print("f")
			print(x)
		y -=  w
		

	# row2 		
	elif dr == 6 and check2(y):
		print("E")
		chance = 'homer'
		if x > px[6] and x <= px[10]:
			x -= (w*dr)
		elif y ==-10 :
			x, y = check_last_row(x, y, dr)
		elif x == px[6]:
			x -=(w*5)
			y -= w
		elif x == px[5]:
			x -= ((w*4)-(w*(dr-5)))
			y -= w
		elif x == px[4]:
			x -= ((w*3)-(w*(dr-4)))
			y -= w
		elif x == px[3]:
			x -=((w*2)-(w*(dr-3)))
			y -= w
		elif x == px[2]:
			x -= (w-(w*(dr-2)))
			y -= w
		elif x == px[1]:
			x += (w*(dr-1))
			y -= w
			
		
	elif dr != 6 and check(y):
		print("R")
		if x in range(px[1], px[5]):
			x += (w*dr)
		elif x == px[5] and dr < 6:
			x += (w*dr)
			print("fo")
		elif x  == px[8] and dr <=2:
			x += (w*dr)
		elif x == px[9] and dr == 1:
			print("meh")
			x += (w*dr)
		elif x == px[7] and dr > 3:				
			x += ((w*3)-(w*(dr-4)))
			y -=w
		elif x == px[8] and dr > 2:
			x += ((w*2)- (w*(dr-3)))
			y -=w
		elif x == px[9] and dr > 1:
			x += ((w*1) - (w*(dr-2)))
			y -=w
		elif x == px[10] and dr > 1:
			x -= (w*(dr-1))
			y -=w
		elif x == px[6] and dr <=4:
			x += (w*dr)
		elif x == px[6] and dr== 5:
			x +=(w*4)
			y -=  w
		elif x == px[7] and dr <=3:
			x += (55*dr)
		elif x == px[10] and dr == 1:
			x = x
			y-=  w

	
	elif dr != 6 and check2(y):
		print("Y")
		if x > px[5] and x <= px[10]:
			x -= (w*dr)
		elif y ==-10 :
			x, y = check_last_row(x, y, dr)
		elif x > px[6] and x <=px[10]:
			x -= (w*dr)
		elif x == px[6]:
			x -= (w*dr)
		elif x == px[2] and dr >=2:
			x -= (w - (w*(dr-2)))
			y -=w
		elif x == px[1]:
			x += (w*(dr-1))
			y -=w
		elif x == px[4] and dr >=4:
			x -= ((w*3)-(w*(dr-4)))
			y -=w
		elif x == px[5] and dr < 5:
			x -= (w*dr)
		elif x == px[5] and dr ==5:
			x -=((w*4) + (w*(dr-5)))
			y -=  w
		elif x == px[4] and dr < 4:
			x -=(w*dr)
		elif x == px[3] and dr <3:
			x -= (w*dr)
		elif x == px[3] and dr!=6:
			x -=((w*2)-(w*(dr-3)))
			y -=w
		elif x == px[2] and dr <2:
			x -= (w*dr)
	
	
	x, y = cs(x, y)	 
	x, y = cl(x, y)	 
	print(x, y, chance)
	return (x, y, chance)
