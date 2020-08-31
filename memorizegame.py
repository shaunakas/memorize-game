import os
import random
print('\n--------Memorizzzeee--------\n')
print('\nLets see how good is your memory\n')
print('You will be shown a word you have to say if it is repeated or not')
words=['Jaipur','Tokyo','Shanghai','Sao Paulo','Pune','Seoul','New york','Florida','Manhattan','Kuala lampur','Birmingham','Mumbai']
clear = lambda: os.system('cls')
repeat=list()
while len(repeat)!=len(words):
	ranword=random.choice(words)
	print('\nYour word is:',ranword)
	ans=input('\nIs the word:\n1.New\n2.Repeated\n')
	if ranword not in repeat:
		if ans=='1':
			repeat.append(ranword)
			clear()
			print('Hurray!!',ranword,'is a new word')
			continue
		elif ans=='2':
			print('you lose the game',ranword,'was a REPEATED word')
			break
		else:
			clear()
			print('Only Enter 1 and 2')
			continue		 
	elif ranword in repeat:
		if ans=='2':
			clear()
			print('You identified it correct its repeated ;)')
			continue
		elif ans=='1':
			print('you lose the game,',ranword,' was a NEW word')
			break
		else:
			clear()
			print('Only Enter 1 and 2')
			continue			
if len(repeat)==len(words):
	print('YOU CLEARED LEVEL 1')
else:
	print('\nEat more Almonds and try another time!!')	









#import os
#clear = lambda: os.system('cls')
#clear()



#import os
#clear = lambda: os.system('cls')
#print('This will dissapear')
#cond=input('put yes or no')
#if cond=='yes':
	#print('Dissapearing')
	#clear()
	#print('Disappeared')
#elif cond=='no':
	#print('Now it will not dissapear')
#else:
	#print("only enter yes or no!!!")	




#use of lambda function
#def myfunc(n):

  #return lambda a : a * n

#mydoubler = myfunc(2)

#print(mydoubler(11))
