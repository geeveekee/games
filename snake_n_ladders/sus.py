def check(y):
	if (y == 495 or y == 385 or y==275 or y ==165 or y==55):
		return True
def check2(y):
	if (y == 440 or y == 330 or y == 220 or y == 110 or y == 0):
		return True

px = {
	1:13,
	2:68,
	3:123,
	4:178,
	5:233,
	6:288,
	7:343,
	8:398,
	9:453,
	10:508
}

snake = {
	(px[6], 495) : (px[3], 495),
	(px[2], 275) : (px[2], 440),
	(px[8], 440) : (px[10], 220),
	(px[5], 275) : (px[5], 330),
	(px[7], 165) : (px[7], 220),
	(px[3], 55) : (px[2], 165),
	(px[6], 165) : (px[4], 0),
	(px[7], 55) : (px[10], 55)
}

ladder = {
	(px[5], 495) : (px[9], 495),
	(px[6], 440) : (px[5], 385),
	(px[3], 440) : (px[1], 110),
	(px[4], 275) : (px[6], 55),
	(px[7], 275) : (px[8], 165),
	(px[3], 165) : (px[3], 110),
	(px[1], 55) : (px[3], 0),
	(px[10], 110) : (px[7], 0)
}

numlist = list(px.keys())
klist_s = list(snake.keys())
vlist_s = list(snake.values())
klist_l = list(ladder.keys())
vlist_l = list(ladder.values())

w = 55

def cs(x, y):
	print('in the function')
	for i in range(0, 8):
		q, w = klist_s[i]
		if q==x and w ==y:
			x, y = vlist_s[i]
	return x, y

def cl(x, y):
	print('in the function')
	for i in range(0, 8):
		q, w = klist_l[i]
		if q==x and w ==y:
			x, y = vlist_l[i]
	return x, y

def check_last_row(x, y, dr):
	for num in range (0, 8):
		if dr >= numlist[num]:
			print("you cant moce foward")
			x = x
			y = y
			print(x, y)
	
	if dr < (list(px.keys())[list(px.values()).index(x)]):
		print(list(px.keys())[list(px.values()).index(x)])
		print(dr)
		print("You can movr from isnside here")
		x -= (55*dr)
		y = y
		print(x, y)
	return x, y

def impostar(x, y, dr):
	
	chance = 'homer'
	
	if x == px[1] and y == 0 :
		x = x
		y = y
		print("You won");

	elif x in range(px[1], px[5]) and dr == 6 and check(y):
		x += (w*dr)
		chance = 'po'

	elif dr == 6 and check(y):
		chance = 'po'
		if x == px[5]:
			x += (w*5)	
		elif x == px[6]:
			x += ((w*4)-(w*(dr-5)))
		elif x == px[7]:
			x += ((w*3)-(w*(dr-4)))
		elif x == px[8]:
			x += ((w*2) - (w*(dr-3)))
		elif x == px[9]:
			x += ((w*1) - (55*(dr-2)))
		elif x == px[10]:
			x -=(w*(dr-1))
		y -=  w
		

	# row2 		
	elif dr == 6 and check2(y):
		chance = 'po'
		if x > px[6] and x <= px[10]:
			x -= (w*dr)
		elif y ==0 :
			x, y = check_last_row(x, y, dr)
		elif x == px[6]:
			x -=(w*5)
			y -= w
		elif x == px[5]:
			x -= ((w*4)-(w*(dr-5)))
			y -=  w
		elif x == px[4]:
			x -= ((w*3)-(w*(dr-4)))
			y -=  w
		elif x == px[3]:
			x -=((w*2)-(w*(dr-3)))
			y -=  w
		elif x == px[2]:
			x -= (w-(w*(dr-2)))
			y -=  w
		elif x == px[1]:
			x += (w*(dr-1))
			y -=  w

		print("the fuck am i back here")
			
		
	elif dr != 6 and check(y):
		if x in range(px[1], px[5]):
			x += (w*dr)
		elif x == px[5] and dr < 6:
			x += (w*dr)
		elif x  == px[8] and dr <=2:
			x += (w*dr)
		elif x == px[9] and dr == 1:
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
		if x > px[5] and x <= px[10]:
			x -= (w*dr)
		elif y ==0 :
			x, y = check_last_row(x, y, dr)
		elif x > px[6] and x <=px[10]:
			x -= (w*dr)
		elif x == px[6]:
			x -= (w*dr)
		elif x == px[2] and dr >=2:
			x -= (w -(w*(dr-2)))
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
		elif x == px[3]  and dr!=6:
			x -=((w*2)-(w*(dr-3)))
			y -=w
		elif x == px[2] and dr <2:
			x -= (w*dr)
		print("the fuck am i back here")
	
	x, y = cs(x, y)	 
	x, y = cl(x, y)
	print(x, y, chance)
	return (x, y, chance)
