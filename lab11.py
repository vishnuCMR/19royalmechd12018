#lets play the game Snake and ladder
import random
a= True 
count=0
def myroll():
	return random.randint(1,6)
while(count<=100):
	n=input("press r to roll the dice:  ")
	if(n=='r'):
		r=myroll()
		count=count+r
		print("you got ", r)
		print("new position is ", count)
	
	if(count==8):
		count=37
		print("i got the ladder")
	elif(count==11):
		count=2
		print("i got snake")
	elif(count==13):
		count=34
		print("i got ladder")
	elif(count==25):
		count=4
		print("i got snake")
	elif(count==38):
		count=9
		print("9")
	elif(count==40):
		count=68
		print("i got ladder")
	elif(count==52):
		count=81
		print("i got ladder")
	elif(count==65):
		count=46
		print("i got snake")
	elif(count==76):
		count=97
		print(" i got ladder")
	elif(count==89):
		count=70
		print(" i got snake")
	elif(count==93):
		count=64
		print("i got snake")
	if (count>=100):
		print("bravo")

	if(count>=100):
		count=count-r
		exit()





