import random
a={1:'rock',2:'paper',3:'scissor'}
while True :
	p=input("your choice rock/paper/scissor")
	c=a[random.randint(1,3)]
	print("you choose:",p,"computer choose",c)
if(p==c):
	print("draw")
elif(p==rock and c==paper):
	print("computer won")